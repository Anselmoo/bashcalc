from decimal import Decimal
from math import *
import subprocess

import subprocess


class TestTerminalInit(object):
    def test_terminal_help(self):
        result = subprocess.call(["bashcalc", "-h"])
        assert not result

    def test_terminal_easy(self):
        expr = "2"
        ref = eval(expr)
        result = subprocess.check_output(["bashcalc", expr])
        assert result == str.encode(f"{ref}\n")

    def test_terminal_add(self):
        expr = "2 + 2"
        ref = Decimal(eval(expr))
        result = subprocess.check_output(["bashcalc", expr])
        assert result == str.encode(f"{ref}\n")

    def test_terminal_complex(self):
        expr = "2 + 2 * exp(2)"
        ref = Decimal(eval(expr))
        result = subprocess.check_output(["bashcalc", expr])
        assert result == str.encode(f"{ref}\n")


class TestTerminalOptions(object):
    def test_terminal_bold(self):
        expr = "2 + 2"
        ref = Decimal(eval(expr))
        result = subprocess.check_output(["bashcalc", expr, "-b"])
        assert result == str.encode(f"\x1b[1m{ref}\n")

    def test_terminal_underling(self):
        expr = "2 + 2"
        ref = Decimal(eval(expr))
        result = subprocess.check_output(["bashcalc", expr, "-u"])
        assert result == str.encode(f"\x1b[4m{ref}\n")

    def test_terminal_red(self):
        expr = "2 + 2"
        ref = Decimal(eval(expr))
        result = subprocess.check_output(["bashcalc", expr, "-c red"])
        assert result == str.encode(f"{ref}\n")


class TestTerminalOutput(object):
    def test_terminal_normal(self):
        expr = "1 / 3"
        ref = Decimal(eval(expr))
        result = subprocess.check_output(["bashcalc", expr])
        assert result == str.encode(f"{ref}\n")

    def test_terminal_round(self):
        expr = "1 / 3"
        ref = round(Decimal(eval(expr)), 4)
        result = subprocess.check_output(["bashcalc", expr, "-r 4"])
        assert result == str.encode(f"{ref}\n")

    def test_terminal_interger(self):
        expr = "1 / 3"
        ref = int(Decimal(eval(expr)))
        result = subprocess.check_output(["bashcalc", expr, "-i"])
        assert result == str.encode(f"{ref}\n")

    def test_terminal_scientifc(self):
        expr = "1 / 3"
        ref = Decimal(eval(expr))
        digits = 5
        result = subprocess.check_output(["bashcalc", expr, f"-s {digits}"])
        assert result == str.encode(f"{ref:.{digits}E}\n")


class TestTerminalError(object):
    def test_name_error(self):
        expr = "ex"
        try:
            result = subprocess.check_output(["bashcalc", expr])
        except subprocess.CalledProcessError:
            assert 1

    def test_type_error(self):
        expr = "1*exp"
        try:
            result = subprocess.check_output(["bashcalc", expr])
        except subprocess.CalledProcessError:
            assert 1

    def test_expression_error(self):
        expr = "1*expp(1)"
        try:
            result = subprocess.check_output(["bashcalc", expr])
        except subprocess.CalledProcessError:
            assert 1
