#!/usr/bin/python3

def multiple_returns(sentence):
    if sentence is None:
        str_len = 0
        first = None
    else:
        if len(sentence):
            str_len = len(sentence)
            first = sentence[0]
        else:
            first = None
            str_len = 0
    return (str_len, first)
