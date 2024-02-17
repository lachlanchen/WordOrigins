import os
import tornado.ioloop
import tornado.web
import json

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.redirect("/word/etymology")  # Redirect to a default word to start.

class WordHandler(tornado.web.RequestHandler):
    def get(self, action):
        image_directory = "static/images"
        images = sorted([f for f in os.listdir(image_directory) if f.endswith(".png")])
        words = [f.rsplit('.', 1)[0] for f in images]
        
        if action not in words:
            if action == "next-word" or action == "prev-word":
                current_word = self.get_argument("word", words[0])  # Default to the first word.
                current_index = words.index(current_word) if current_word in words else 0
                if action == "next-word":
                    next_index = (current_index + 1) % len(words)
                else:
                    next_index = (current_index - 1) % len(words)
                word_to_show = words[next_index]
            else:
                word_to_show = words[0]  # Fallback to the first word.
        else:
            word_to_show = action  # The action is a valid word.
        
        self.render("index.html", word=word_to_show, images=[f"{word_to_show}.png"], words=words)

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
