# DNA -> RNA Transcription


def transcribe(seq: str) -> str:
    """
    TODO: transcribes DNA to RNA by generating
    the complement sequence with T -> U replacement
    """
    transcript = []
    for base in seq:
        if base == "A":
            transcript.append("U")
        elif base == "T":
            transcript.append("A")
        elif base == "G":
            transcript.append("C")
        elif base == "C":
            transcript.append("G")
    return transcript

def reverse_transcribe(seq: str) -> str:
    """
    TODO: transcribes DNA to RNA then reverses
    the strand
    """
    transcript = []
    for base in seq:
        if base == "A":
            transcript.append("U")
        elif base == "T":
            transcript.append("A")
        elif base == "G":
            transcript.append("C")
        elif base == "C":
            transcript.append("G")

    #transcript.reverse()
    rev_transcript = transcript[::-1]
    return rev_transcript

