# -*- coding: utf-8 -*-
import sys
from unittest.mock import patch

import pytest

from dvnv.dvnv import parse_args


def test_parse_args_pass():
    with patch.object(sys, "argv", ["dvnv", "python", "dvnv"]):
        args = parse_args()
        assert args.lang == "python"
        assert args.name == "dvnv"


def test_parse_args_no_args(capsys):
    with patch.object(sys, "argv", ["dvnv", None, None]):
        with pytest.raises(SystemExit):
            parse_args()
            captured = capsys.readouterr()
            assert (
                captured.err
                == "[ERR] the following arguments are required: lang, name\n"
            )


def test_parse_args_no_lang(capsys):
    with patch.object(sys, "argv", ["dvnv", None, "test-project"]):
        with pytest.raises(SystemExit):
            parse_args()
            captured = capsys.readouterr()
            assert captured.err == "[ERR] the following arguments are required: lang\n"


def test_parse_args_no_name(capsys):
    with patch.object(sys, "argv", ["dvnv", "python", None]):
        with pytest.raises(SystemExit):
            parse_args()
            captured = capsys.readouterr()
            assert captured.err == "[ERR] the following arguments are required: name\n"


def test_parse_args_install_scripts():
    with patch.object(sys, "argv", ["dvnv", None, None, "--install_scripts"]):
        assert parse_args()
