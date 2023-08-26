#include <iostream>
#include <chrono>

#include "antlr4-runtime.h"
#include "antlr/PslLexer.h"
#include "antlr/PslParser.h"

#include <Windows.h>

using namespace antlr4;

int main(int argc, const char *argv[])
{
    std::chrono::high_resolution_clock::time_point startTime, endTime;
    for (int i = 0; i < 10; i++)
    {
        startTime = std::chrono::high_resolution_clock::now();
        auto src = std::ifstream();
        src.open("D:/科研项目/PhotLab/phot-lang/demo/prjs/roft/roft.psl");
        ANTLRInputStream input(src);
        PslLexer lexer(&input);
        CommonTokenStream tokens(&lexer);
        PslParser parser(&tokens);
        tree::ParseTree *tree = parser.program();
        endTime = std::chrono::high_resolution_clock::now();
        auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(endTime - startTime).count();
        std::cout << "函数运行时间：" << duration << " 毫秒" << std::endl;
    }

    // auto s = tree->toStringTree(&parser);
    // std::cout << "Parse Tree: " << s << std::endl;

    return 0;
}