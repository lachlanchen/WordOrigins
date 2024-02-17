import os
import tornado.ioloop
import tornado.web
from word_etymology_analyzer import WordEtymologyAnalyzer  # Ensure this matches your actual import
from etymology_graph import EtymologyGraph  # Ensure this matches your actual import
import json

# Ensure these directories exist
json_directory = "jsons"
image_directory = "static/images"
if not os.path.exists(json_directory):
    os.makedirs(json_directory)
if not os.path.exists(image_directory):
    os.makedirs(image_directory)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html", images=[])

class WordHandler(tornado.web.RequestHandler):
    def get(self, word):
        # Analyze word and generate image
        analyzer = WordEtymologyAnalyzer(use_cache=True)
        analysis_result = analyzer.analyze_word_etymology(word)
        json_path = os.path.join(json_directory, f"{word}.json")
        with open(json_path, 'w') as f:
            json.dump(analysis_result, f)
        
        # Assuming the graph class can take the json_path and save an image to a specified path
        graph = EtymologyGraph(json_path)
        image_path = os.path.join(image_directory, f"{word}.png")
        graph.plot_graph(save_path=image_path)
        
        # Retrieve all images for the carousel
        # images = [f for f in os.listdir(image_directory) if f.endswith(".png")]
        images = [f for f in os.listdir(image_directory) if f.startswith(word) and f.endswith(".png")]
        images = sorted(images)  # Optional: Sort or customize order
        
        # Check if it's an AJAX request
        if self.request.headers.get("X-Requested-With") == "XMLHttpRequest":
            images = [f for f in os.listdir(image_directory) if f.endswith(".png")]
            images.sort()  # Optional: customize the sorting
            self.render("carousel_items.html", images=images)
        else:
            self.render("index.html", images=images)

# def make_app():
#     return tornado.web.Application([
#         (r"/", MainHandler),
#         (r"/word/(.*)", WordHandler),
#     ], debug=True, static_path=os.path.join(os.path.dirname(__file__), "static"), template_path=os.path.join(os.path.dirname(__file__), "templates"))

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/word/(.*)", WordHandler),
    ], debug=True, 
    static_path=os.path.join(os.path.dirname(__file__), "static"), 
    template_path=os.path.join(os.path.dirname(__file__), "templates"))


if __name__ == "__main__":
    app = make_app()
    app.listen(7788)
    print("Server running on http://localhost:7788")
    tornado.ioloop.IOLoop.current().start()
