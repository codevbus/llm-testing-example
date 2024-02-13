#!/usr/bin/env python


import os
import pytest
import string
from spellchecker import SpellChecker
from main import CommaSeparatedListOutputParser, template

os.getenv("OPENAI_API_KEY")


@pytest.fixture
def parser():
    return CommaSeparatedListOutputParser()


@pytest.fixture
def spell():
    return SpellChecker()


@pytest.fixture
def template_spellcheck(spell):
    # Remove punctuation from the template string and then split it into words
    translator = str.maketrans("", "", string.punctuation)
    no_punctuation_template = template.translate(translator)
    words = no_punctuation_template.split()

    misspelled = spell.unknown(words)
    assert (
        not misspelled
    ), f"The template contains the following misspelled words: {', '.join(misspelled)}"


def test_parse_with_valid_input(parser, spell):
    input_text = "red, blue, green, yellow, purple"
    expected_output = ["red", "blue", "green", "yellow", "purple"]
    assert parser.parse(input_text) == expected_output
    assert not spell.unknown(expected_output)


def test_parse_with_empty_input(parser):
    input_text = ""
    expected_output = [""]
    assert parser.parse(input_text) == expected_output


def test_parse_with_single_element(parser, spell):
    input_text = "red"
    expected_output = ["red"]
    assert parser.parse(input_text) == expected_output
    assert not spell.unknown(expected_output)


def test_spellchecking_colors(spell):
    colors = ["red", "blue", "green", "yellow", "purple"]
    misspelled = spell.unknown(colors)
    assert (
        not misspelled
    ), f"The following colors are misspelled: {', '.join(misspelled)}"


def test_template_spelling(template_spellcheck):
    pass
