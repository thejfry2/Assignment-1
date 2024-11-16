# write tests for parsers

from seqparser import (
        FastaParser,
        FastqParser)
aparser = FastaParser('data/test.fa')
qparser = FastqParser('data/test.fq')

def test_freebie_parser_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True


def test_freebie_parser_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_FastaParser():
    """
    TODO: Write your unit test for your FastaParser
    class here. You should generate an instance of
    your FastaParser class and assert that it properly
    reads in the example Fasta File.
    """
        #this code block calls the parser to read the first two lines of test.fa and record them
        #then it goes back to the beggining of the file and reads the first two lines with readline()
        #then it asserts that they are the same to make sure that the parser reads the lines right
    with open("data/test.fa", "r") as file:
        first_two_lines = aparser.get_record(file)
        first_line = first_two_lines[0].strip()
        second_line = first_two_lines[1].strip()
        file.seek(0)
        first_line_again = file.readline().strip()
        second_line_again = file.readline().strip()
        assert first_line == first_line_again, "parser error"
        assert second_line == second_line_again, "parser error"

    pass


def test_FastqParser():
    """
    TODO: Write your unit test for your FastqParser
    class here. You should generate an instance of
    your FastqParser class and assert that it properly
    reads in the example Fastq File.
    """
    #this code block works the same as the first one, only it is calling fastqparser and test.fq
    with open("data/test.fq", "r") as file:
        first_two_lines = qparser.get_record(file)
        first_line = first_two_lines[0].strip()
        second_line = first_two_lines[1].strip()
        file.seek(0)
        first_line_again = file.readline().strip()
        second_line_again = file.readline().strip()
        assert first_line == first_line_again, "parser error"
        assert second_line == second_line_again, "parser error"
    pass

test_FastaParser()
test_FastqParser()