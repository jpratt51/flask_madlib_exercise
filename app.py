from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import s1, s2, s3, s4, s5

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)


@app.route('/')
def pick_story():
    """Lists story templates for user to choose from"""
    return render_template('story_form.html')

stories = {"s1": s1, "s2": s2, "s3": s3, "s4": s4, "s5": s5}

story_titles = {"s1": "Once Upon A Time", "s2": "Majestic Animal", "s3": "Nature Story", "s4": "Pizza Pizza", "s5": "Computers"}

@app.route('/question-form')
def question_form():
    """generates question form"""
    story = request.args["story"]
    title = story_titles[story]
    template = stories[story]
    words = template.words
    return render_template('questions.html', words=words, title=title, story=story)

@app.route('/story/<story>')
def generate_story(story):
    """generates story instance from users answers"""
    template = stories[story]
    answers = template.generate(request.args)
    return render_template('story.html', answers=answers)