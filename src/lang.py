import sys
from antlr4 import FileStream
from front import parseSource

import time


def timeTest():
    src = FileStream("D:\\科研项目\\PhotLab\\phot-lang\\demo\\prjs\\roft\\roft.psl")
    # src = FileStream("D:\\科研项目\\PhotLab\\phot-lang\\demo\\feat\\anno.psl")
    # src = FileStream("D:\\科研项目\\PhotLab\\phot-lang\\demo\\feat\\varies.psl")
    tree = parseSource(src)


if __name__ == '__main__':
    # src = FileStream(sys.argv[1])
    # tree = parseSource(src)
    # print(tree)
    start = time.time()
    for i in range(1):
        timeTest()
    end = time.time()
    print(end - start)
