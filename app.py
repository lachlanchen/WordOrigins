import os
import tornado.ioloop
import tornado.web
import json

import os
import tornado.ioloop
import tornado.web
import json
from word_etymology_analyzer import WordEtymologyAnalyzer  # Ensure this matches your actual import
from etymology_graph import EtymologyGraph  # Ensure this matches your actual import

import os
import tornado.ioloop
import tornado.web
import base64
from PIL import Image
import io
import json


json_directory = "jsons"
image_directory = "static/images"
if not os.path.exists(json_directory):
    os.makedirs(json_directory)
if not os.path.exists(image_directory):
    os.makedirs(image_directory)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.redirect("/word/etymology")  # Redirect to a default word to start.

class GetWordEtymologyHandler(tornado.web.RequestHandler):
    def get_image_as_base64_string(self, image_path):
        with Image.open(image_path) as image:
            buffered = io.BytesIO()
            image.save(buffered, format="PNG")
            return base64.b64encode(buffered.getvalue()).decode()

    def generate_etymology_image(self, word):
        # Your existing logic to analyze the word and generate the image
        analyzer = WordEtymologyAnalyzer(use_cache=True)
        analysis_result = analyzer.analyze_word_etymology(word)
        json_path = os.path.join(json_directory, f"{word}.json")
        with open(json_path, 'w') as f:
            json.dump(analysis_result, f)

        graph = EtymologyGraph(json_path)
        image_path = os.path.join(image_directory, f"{word}.png")
        graph.plot_graph(save_path=image_path)
        return image_path

    def get(self, word):
        # image_directory = "static/images"
        # image_path = os.path.join(image_directory, f"{word}.png")
        image_path = f"{word}.png"

        if word:
            word = word.lower()

        # Check if the image exists; if not, generate it
        if not os.path.exists(image_path):
            image_path = self.generate_etymology_image(word)

        image_base64 = self.get_image_as_base64_string(image_path)
        self.write({"status": "success", "word": word, "image": image_base64})

    def post(self):
        data = tornado.escape.json_decode(self.request.body)
        word = data.get("word", "")

        if word:
            word = word.lower()

        if not word:
            self.write({"status": "error", "message": "No word provided"})
            return

        # image_path = os.path.join(image_directory, f"{word}.png")
        image_path = f"{word}.png"

        # Check if the image exists; if not, generate it
        if not os.path.exists(image_path):
            image_path = self.generate_etymology_image(word)

        image_base64 = self.get_image_as_base64_string(image_path)
        self.write({"status": "success", "word": word, "image": image_base64})



class WordHandler(tornado.web.RequestHandler):
    def get(self, action):
        # image_directory = "static/images"
        images = sorted([f for f in os.listdir(image_directory) if f.endswith(".png")])
        words = [f.rsplit('.', 1)[0] for f in images]
        
        current_word = self.get_argument("word", None)

        if current_word:
            current_word = current_word.lower()

        if action == "next-word" or action == "prev-word":
            if not current_word or current_word not in words:
                current_word = words[0]  # Default to the first word if not specified or not found.
            current_index = words.index(current_word)
            if action == "next-word":
                next_index = (current_index + 1) % len(words)
            else:  # "prev-word"
                next_index = (current_index - 1) % len(words)
            word_to_show = words[next_index]
        elif action in words:
            word_to_show = action
        else:
            word_to_show = action
            # Generate the image if it does not exist
            self.generate_word_image(word_to_show)

        # image_path = os.path.join(image_directory, f"{word_to_show}.png")
        image_path = f"{word_to_show}.png"
        self.render("index.html", word=word_to_show, images=[image_path], words=words)

    def generate_word_image(self, word):
        analyzer = WordEtymologyAnalyzer(use_cache=True)
        analysis_result = analyzer.analyze_word_etymology(word)
        json_path = os.path.join(json_directory, f"{word}.json")
        with open(json_path, 'w') as f:
            json.dump(analysis_result, f)

        graph = EtymologyGraph(json_path)
        image_path = os.path.join(image_directory, f"{word}.png")
        if not os.path.exists(image_path):  # Check if the image already exists to avoid re-generation
            graph.plot_graph(save_path=image_path)


# Update the make_app function to include the new API endpoint
def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/word/(.*)", WordHandler),
        (r"/get_word_etymology/(.*)", GetWordEtymologyHandler),
    ], debug=True, 
    static_path=os.path.join(os.path.dirname(__file__), "static"), 
    template_path=os.path.join(os.path.dirname(__file__), "templates"))


if __name__ == "__main__":
    app = make_app()
    app.listen(7788)
    print("Server running on http://localhost:7788")
    tornado.ioloop.IOLoop.current().start()
