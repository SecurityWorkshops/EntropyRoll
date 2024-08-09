from flask import Flask, render_template

app = Flask(__name__)

slides = [
    {
        "title": "Diceware- Rolling your own encryption",
        "content": ["This is the first slide", "You can add bullet points", "And more text"],
        "background_color": "#041e00",  # Default to a blue color
        "background_image": None,  # Set to a URL or path to an image
    },
    {
        "title": "Slide 2",
        "content": ["Second slide content", "More text here", "Even more bullet points"],
        "background_color": "#2ecc71",  # Default to a green color
        "background_image": None,  # Or set a background image here
    },
    {
        "title": "Slide 3",
        "content": ["Second slide content", "More text here", "Even more bullet points"],
        "background_color": "#3498db",  # Default to a green color
        "background_image": None,  # Or set a background image here
    },
    {
        "title": "Slide 4",
        "content": ["Second slide content", "More text here", "Even more bullet points"],
        "background_color": "#041e00",  # Default to a green color
        "background_image": None,  # Or set a background image here
    },
    # Add more slides as needed
]

@app.route('/')
def slideshow():
    return render_template('slide.html', slides=slides)

if __name__ == '__main__':
    app.run(debug=True)
