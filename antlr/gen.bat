@echo off

set "info=[32m"
set "end=[0m"

@echo %info%Generating antlr parser for python...%end%
@echo Output dir is "../src/front/antlr".
java -jar antlr-4.13.0-complete.jar -Dlanguage=Cpp Psl.g4 -no-listener -visitor -o "../src/antlr"

@echo %info%Deleting PslVisitor.py as it's of little use...%end%
@REM del ..\legacy\front\antlr\PslVisitor.py
@echo Deleted PslVisitor.py successfully.

@REM @echo %info%Formatting python codes using pycharm.bat...%end%
@REM pycharm.bat format -m *.py "../src/front/antlr" -allowDefaults | findstr /b "Formatting"
@REM @echo %info%All tasks completed.%end%