# -*- coding: utf-8 -*-
from dvnv.utils import print_error


def test_print_error(capsys):
    print_error("To stderr")
    captured = capsys.readouterr()
    assert captured.err == "[ERR] To stderr\n"
