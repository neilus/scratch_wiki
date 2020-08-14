import pytest

class Paragraph:
    type:str = ""
    lines:str = ""

    def __str__(self):
        return f"{self.type}: {self.lines}"


def parser(input:str):
    """
    Gets a multiline string as an input
    Returns a list of sections
    """

    ret = []
    lines = input.split("\n")
    paragraph = None
    for i in range(0, len(lines)):
        if "##" in lines[i]:
            if paragraph is not None:
                ret.append(paragraph)
            paragraph = Paragraph()
            paragraph.type = lines[i].strip()
        elif paragraph is not None:
            paragraph.lines += lines[i]

    ret.append(paragraph)
    return ret

input = """
asdiufasdljfbsad
    ##c
    valami

    megvalami
    ##c
    masvalami
"""

def test_parsed_is_not_none():
    parsed = parser("")

    assert parsed is not None


def test_simple_section():
    # Given
    input = """
    ##c
    valami
    """

    parsed = parser(input)

    assert len(parsed) == 1
    assert "valami" in parsed[0].lines

def test_complicated_sections():
    parsed = parser(input)

    assert len(parsed) == 2
    assert "valami" in parsed[0].lines
    assert "megvalami" in parsed[0].lines
    assert "masvalami" in parsed[1].lines

def test_type_of_sections():
    parsed = parser(input)

    assert parsed[0].type == "##c"
