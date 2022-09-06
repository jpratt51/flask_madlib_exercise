"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, prompt:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, words, text):
        """Create story with words and template text."""

        self.words = words
        self.text = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.text

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started

s1 = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)
s2 = Story(
    ["animal", "country", "plural_noun", "a_food", "type_of_screen_device","noun","verb","verb_2","adjective"],
    """The majestic {animal} has roamed the forests of {country} for thousands of years. Today, she wanders in search of {plural_noun}. She must find food to survive. While hunting for {a_food}, she found a/an {type_of_screen_device} hidden behind a {noun}. She has never seen anything like this before. What will she do? With the device in her teeth, she tries to {verb}, but nothing happens. She takes it back to her family. When her family sees it, they quickly {verb_2}. Soon, the device becomes {adjective}, and the family decides to put it back where they found it."""
)
s3 = Story(
    ["adjective", "adjective_2", "type_of_bird", "room_in_a_house", "verb_past_tense","verb","relatives_name","noun","a_liquid","verb_ending_in_ing","part_of_the_body_plural","plural_noun","verb_ending_in_ing_2","noun_2"],
    """It was a {adjective}, cold November day. I woke up to the {adjective_2} smell of {type_of_bird} roasting in the {room_in_a_house} downstairs. I {verb_past_tense} down the stairs to see if I could help {verb} the dinner. My mom said, "See if {relatives_name} needs a fresh {noun}." So I carried a tray of glasses full of {a_liquid} into the {verb_ending_in_ing} room. When I got there, I couldn't believe my {part_of_the_body_plural}! There were {plural_noun} {verb_ending_in_ing_2} on the {noun_2}!"""
)
s4 = Story(
    ["adjective", "nationality", "person", "noun", "adjective_2","noun_2","adjective_3","adjective_4","plural_noun","noun_3","number","shapes","food","food_2","number_2"],
    """Pizza was invented by a {adjective} {nationality} chef named {person}. To make a pizza, you need to take a lump of {noun}, and make a thin, round {adjective_2} {noun_2}. Then you cover it with {adjective_3} sauce, {adjective_4} cheese, and fresh chopped {plural_noun}. Next you have to bake it in a very hot {noun_3}. When it is done, cut it into {number} {shapes}. Some kids like {food} pizza the best, but my favorite is the {food_2} pizza. If I could, I would eat pizza {number_2} times a day!"""
)
s5 = Story(
    ["noun", "plural_noun", "verb_present_tense_1", "verb_present_tense_2", "part_of_body_small", "adjective_1", "plural_noun_2", "adjective_2"],
    """Today, every student has a computer small enough to fit into her {noun}. She can solve any math problem by simply pushing the computer's little {plural_noun}. Computers can add, multiply, divide, and {verb_present_tense_1}. They can also {verb_present_tense_2} better than a human. Some computers are {part_of_body_small}. Others have a/an {adjective_1} screen that shows all kinds of {plural_noun_2} and {adjective_2} figures."""
)
