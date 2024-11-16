# write tests for transcribes

from seqparser import (
        FastaParser,
        FastqParser,
        transcribe,
        reverse_transcribe,
        )
aparser = FastaParser('data/test.fa')
qparser = FastqParser('data/test.fq')

from seqparser.seq import (transcribe,reverse_transcribe)





def test_freebie_transcribe_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True


def test_freebie_transcribe_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_transcribe():
    """
    TODO: Write your unit test for the
    transcribe function here.
    """
    #the following code block reads the first 2 lines of test.fa, gets the sequence then transcribes it.
    #then it peforms the inverse of transcription, converts the orignial seq into the same format and asserts that they are the same.
    #this is so you can see if transcription as failed or altered the data at all. 
    with open("data/test.fa", "r") as file:
        first_two_lines = aparser.get_record(file)
        second_line = first_two_lines[1].strip()
        second_line_trans = transcribe(second_line)
        transcript = []
        for base in second_line_trans:
            if base == "A":
                transcript.append('T')
            if base == 'U':
                transcript.append('A')
            if base == 'G':
                transcript.append('C')
            if base == 'C':
                transcript.append('G')
        origin_transcript = []
        for base in second_line:
            origin_transcript.append(base)

        assert origin_transcript == transcript

    pass


def test_reverse_transcribe():
    """
    TODO: Write your unit test for the
    reverse transcribe function here.
    """
    # this unit test works the same way as the first, by preforming the rev transcript operation 
    #the the reverse of that operation and comparing the results. I chose to do it this way so that it is
    #more generalizable than just checking a refrence file. 
    with open("data/test.fa", "r") as file:
        first_two_lines = aparser.get_record(file)
        seq = first_two_lines[1].strip()
        tran = reverse_transcribe(seq)
        transcript = []
        for base in tran:
            if base == "A":
                transcript.append('T')
            if base == 'U':
                transcript.append('A')
            if base == 'G':
                transcript.append('C')
            if base == 'C':
                transcript.append('G')
        transcript.reverse()
        origin_transcript = []
        for base in seq:
            origin_transcript.append(base)
        
        assert origin_transcript == transcript
    pass

test_reverse_transcribe()
test_transcribe()
"""second_line_re_trans_corrected = []
        for base in second_line_re_trans:
            if base == "U":
                second_line_re_trans_corrected.append("T")
            if base == "'" or base == "," or base == "[" or base == "]" or base == " ":
                continue
            else:
                second_line_re_trans_corrected.append(base)"""