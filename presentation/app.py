from flask import Flask, render_template

app = Flask(__name__)

slides = [
    {
        "title": "Diceware- Rolling your own encryption",
        "content": [
    "Randomness Rocks: Discover why a little chaos makes your keys super secure.",
    "Get Rolling: Learn how to craft your own keys with a few rolls of the dice.",
    "From Dice to Devices: Endless possibilites"
],
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


bitcoin_slides =  [
    {
        "title": "Diceware- Rolling your own encryption",
        "content": [
    "Randomness Rocks: Discover why a little chaos makes your keys super secure.",
    "Get Rolling: Learn how to craft your own keys with a few rolls of the dice.",
    "From Dice to Devices: Endless possibilites"
],
        "background_color": "#041e00",  # Default to a blue color
        "background_image": None,  # Set to a URL or path to an image
    },
]


@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

@app.route('/')
def slideshow():
    return render_template('slide.html', slides=slides)



@app.route('/bitcoin')
def bitcoin():
    return render_template('slide.html', slides=bitcoin_slides)

if __name__ == '__main__':
    app.run(debug=True)
