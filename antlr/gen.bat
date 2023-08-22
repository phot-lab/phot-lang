@echo off
@echo generate antlr parser for python.
java -jar antlr-4.13.0-complete.jar -Dlanguage=Python3 Psl.g4 -no-listener -visitor -o "../src/front/antlr"
@echo delete PslVisitor.py as it's of little use.
del ..\src\front\antlr\PslVisitor.py
@echo format python codes using pycharm.bat.
pycharm.bat format -m *.py "../src/front/antlr" -allowDefaults