
import matplotlib.pyplot as plt
import matplotlib


# Set a font that supports both Arabic and CJK characters
# Example: 'Noto Sans CJK JP' or 'Arial Unicode MS'
# Make sure the font is installed on your system.
matplotlib.rcParams['font.family'] = 'Arial Unicode MS'



import json
import math
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from cjkwrap import wrap
from PIL import Image, ImageDraw, ImageFont

from matplotlib.font_manager import FontProperties
from pprint import pprint

import os

# # Use the font name directly if it's installed system-wide
# universal_font = FontProperties(fname='Noto Sans CJK Regular/Noto Sans CJK Regular.otf')
# arabic_font = FontProperties(fname='Noto_Sans,Noto_Sans_Arabic/Noto_Sans_Arabic/NotoSansArabic-VariableFont_wdth,wght.ttf')

# Assuming these are the correct paths on your system
cjk_font_path = 'Noto Sans CJK Regular/Noto Sans CJK Regular.otf'
arabic_font_path = 'Noto_Sans,Noto_Sans_Arabic/Noto_Sans_Arabic/NotoSansArabic-VariableFont_wdth,wght.ttf'

# Initialize FontProperties with the full paths
cjk_font = FontProperties(fname=cjk_font_path)
arabic_font = FontProperties(fname=arabic_font_path)

def get_font_for_language(language):
    # Map languages to their corresponding fonts
    language_font_map = {
        'japanese': cjk_font,
        'chinese': cjk_font,
        'arabic': arabic_font,
        # Add more mappings as necessary
        'french': cjk_font,  # Assuming the universal font supports French
    }
    print("language: ", language_font_map.get(language) )
    
    return language_font_map.get(language)  # Default to universal font


class EtymologyGraph:
    def __init__(self, filepath):
        self.G = nx.DiGraph()
        self.pos = {}
        self.depths = {}
        self.nodes_by_depth = {}
        self.radius_increment = 2
        self.reserved_angle = 30
        self.rotation_offset = 90
        self.initial_angle = 45
        self.load_data(filepath)
        self.assign_ids(self.etymology_data)
        self.add_to_graph(self.etymology_data)
        self.calculate_depths(0)  # Assuming the root node has ID 0
        self.calculate_positions()

    def load_data(self, filepath):
        with open(filepath, "r") as fd:
            self.etymology_data = json.load(fd)

    def assign_ids(self, data, current_id=0):
        data['id'] = current_id
        current_id += 1
        for part in data.get('etymology', []):
            current_id = self.assign_ids(part, current_id)
        return current_id

    def add_to_graph(self, data, parent=None):
        node_id = data['id']
        node_label = data.get('part', data.get('word', ''))
        node_data = {key: data.get(key, '') for key in ['part', 'language', 'meaning', 'example_words', 'synonyms_in_other_languages']}
        self.G.add_node(node_id, **node_data, label=node_label)
        if parent is not None:
            self.G.add_edge(parent, node_id)
        for child in data.get('etymology', []):
            self.add_to_graph(child, node_id)

    def calculate_depths(self, node, depth=0):
        self.depths[node] = depth
        for successor in self.G.successors(node):
            self.calculate_depths(successor, depth + 1)

    def calculate_positions(self):
        for node, depth in self.depths.items():
            self.nodes_by_depth.setdefault(depth, []).append(node)
        self.position_nodes()

    def radians_to_degrees(self, radians):
        return radians * (180 / math.pi)

    def adjust_angle(self, angle, depth, index, total_siblings):
        half_reserved = self.reserved_angle / 2
        if 0 <= angle < 180:
            adjusted_angle = (angle - half_reserved) * ((180 - self.reserved_angle) / 180) + half_reserved
        elif 180 <= angle < 360:
            adjusted_angle = ((angle - 180) - half_reserved) * ((180 - self.reserved_angle) / 180) + 180 + half_reserved
        else:
            adjusted_angle = angle
        if depth > 1 and total_siblings > 1:
            parent_sector_angle = (360 - self.reserved_angle) / (total_siblings - 1)
            adjusted_angle = (parent_sector_angle * index) + (adjusted_angle if adjusted_angle < 180 else adjusted_angle - 360)
        return adjusted_angle



    def position_nodes(self):
        depths = {}
        nodes_by_depth = {}
        def calculate_depths(node, depth=0):
            depths[node] = depth
            for successor in self.G.successors(node):
                calculate_depths(successor, depth + 1)

        calculate_depths(0)  # Assuming the root node has ID 0

        for node, depth in depths.items():
            nodes_by_depth.setdefault(depth, []).append(node)

        radius_increment = 2
        reserved_angle = 30  # Reserved angle for the horizontal region for all nodes
        initial_angle = 45  # Initial location adjustment

        def adjust_angle(angle, depth, index, total_siblings):
            half_reserved = reserved_angle / 2
            if 0 <= angle < 180:
                adjusted_angle = (angle - half_reserved) * ((180 - reserved_angle) / 180) + half_reserved
            elif 180 <= angle < 360:
                adjusted_angle = ((angle - 180) - half_reserved) * ((180 - reserved_angle) / 180) + 180 + half_reserved
            else:
                adjusted_angle = angle
            if depth > 1 and total_siblings > 1:
                parent_sector_angle = (360 - reserved_angle) / (total_siblings - 1)
                adjusted_angle = (parent_sector_angle * index) + (adjusted_angle if adjusted_angle < 180 else adjusted_angle - 360)
            return adjusted_angle

        for depth, nodes in nodes_by_depth.items():
            radius = depth * radius_increment
            if depth == 0:
                self.pos[0] = (0, 0)
                continue
            if depth == 1:
                angle_increment = (360 - reserved_angle) / max(len(nodes), 1)
                for i, node in enumerate(nodes):
                    angle = initial_angle + i * angle_increment
                    adjusted_angle = adjust_angle(angle, depth, i, len(nodes))
                    self.pos[node] = (radius * np.cos(np.radians(adjusted_angle)), radius * np.sin(np.radians(adjusted_angle)))
            else:
                for i, node in enumerate(nodes):
                    parent = list(self.G.predecessors(node))[0]
                    parent_pos = self.pos[parent]
                    parent_angle = np.degrees(np.arctan2(parent_pos[1], parent_pos[0]))
                    siblings = list(self.G.successors(parent))
                    index = siblings.index(node)
                    total_siblings = len(siblings)
                    adjusted_angle = adjust_angle(parent_angle, depth, index, total_siblings)
                    self.pos[node] = (radius * np.cos(np.radians(adjusted_angle)), radius * np.sin(np.radians(adjusted_angle)))

        # Printing positions for verification
        for node, position in self.pos.items():
            node_label = 'root' if node == 0 else self.G.nodes[node]['label']
            print(f"Node {node_label} position: {position}")


    def plot_graph(self, save_path=None):
        plt.figure(figsize=(15, 10))
        node_colors = ["lightblue" if node != 0 else "yellow" for node in self.G.nodes()]
        nx.draw_networkx_nodes(self.G, self.pos, node_size=3000, node_color=node_colors, alpha=0.8)
        nx.draw_networkx_edges(self.G, self.pos, arrowstyle="<|-", arrowsize=30, edge_color="black")
        self.draw_labels()
        plt.axis('off')
        if save_path:
            plt.savefig(save_path, format='png', bbox_inches='tight')
        plt.show()

    def draw_labels(self):
        # Draw edge labels with language information
        edge_labels = {(source, target): f"{self.G.nodes[target]['language']}" for source, target in self.G.edges()}
        nx.draw_networkx_edge_labels(self.G, self.pos, edge_labels=edge_labels, font_color='green', font_size=14)
        
        for node, (x, y) in self.pos.items():
            if node == 0:  # For the root node
                word = self.etymology_data['word']
                plt.text(x, y, word, fontsize=30, ha='center', va='center', fontweight="bold")
                
                synonyms = self.G.nodes[node].get('synonyms_in_other_languages', '')
                synonyms_text = synonyms if type(synonyms) is str else ", ".join([v for k,v in synonyms.items() if k in ["arabic", "japanese", "chinese"]])
                
                
                pprint(synonyms)
                print(synonyms_text)
                
                # # plt.text(x, y - 0.5, synonyms_text, fontsize=18, ha='center', va='center', fontproperties=universal_font)
                plt.text(x, y + 0.3, synonyms_text, fontsize=18, ha='center', va='center', color="gray")
                
                # plot_synonyms_text(x, y-0.5, synonyms, plt)
                
            else:
                # Label (word itself)
                # label = self.G.nodes[node].get('label', '')
                # plt.text(x, y, label, fontsize=24, ha='center', va='center')

                # Part (with different font size and optionally different color)
                part = self.G.nodes[node].get('part', '')
                if part:
                    plt.text(x, y, f"{part}", fontsize=24, ha='center', va='center', color='black', fontweight="bold")  # Adjust color as needed

                # Meaning (with different font size and color)
                meaning = self.G.nodes[node].get('meaning', '')
                if meaning:
                    
                    meaning = meaning.split(",")[:2]
                    meaning = ",".join(meaning)
                    meaning_wrapped = wrap(meaning, 10)[:2]
                    n_wrapped = len(meaning_wrapped)
                    meaning = "\n".join(meaning_wrapped)
                    plt.text(x, y + 0.25 * (n_wrapped+1)/2, f"{meaning}", fontsize=14, ha='center', va='center', color='crimson', fontweight='bold')  # Adjust color as needed

                # Examples (with different font size and color)
                examples = self.G.nodes[node].get('example_words', [])
                
                if examples:
                    example_truncated = examples[:2]
                    n_example = len(example_truncated)
                    example_text = ", ".join(example_truncated)
                    # example_text = "\n".join(wrap(example_text, 20)[:1])
                    
                    plt.text(x, y - 0.3 * n_example/2, f"{example_text}", fontsize=18, ha='center', va='center', color='black')  # Adjust color as needed

    

        # Edge labels with the same approach as before
        for edge in self.G.edges:
            source, target = edge
            source_pos, target_pos = self.pos[source], self.pos[target]
            dx, dy = target_pos[0] - source_pos[0], target_pos[1] - source_pos[1]
            angle = np.degrees(np.arctan2(dy, dx)) + 180
            # edge_label = f"{self.G.nodes[target]['language']} --> {self.G.nodes[source]['language']}"
            # edge_label = f"{self.G.nodes[target]['language']}"
            x, y = (source_pos[0] + target_pos[0]) / 2, (source_pos[1] + target_pos[1]) / 2
            # plt.text(x, y, edge_label, rotation=angle, rotation_mode='anchor', fontsize=14, color='red', ha='center', va='center')



if __name__ == "__main__":

    

    def process_and_save_graphs(json_directory):
        for filename in os.listdir(json_directory):
            if filename.endswith(".json"):
                json_path = os.path.join(json_directory, filename)
                image_path = os.path.splitext(json_path)[0] + ".png"
                
                print(f"Processing {json_path}...")
                graph = EtymologyGraph(json_path)
                graph.plot_graph(save_path=image_path)
                print(f"Saved image to {image_path}")

    # Example usage:
    json_directory = "jsons"
    process_and_save_graphs(json_directory)
