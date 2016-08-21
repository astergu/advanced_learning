/*
 * 设计病实现一个通用的词表解析器
 * Content:
 *  <col1>\t<col2>\t...\t<coln>
 *
 * 每一行都是一条记录，每一列可能的类型包括：
 * int
 * float
 * char*
 * 形如num:item1, item2, item3的数组
 * 其他用户自定义类型（需要灵活支持多种自定义类型）
 *
 * 每一列的数据中均不包含\t字符，每一行以\n结尾。
 */

#include <iostream>
#include <fstream>
#include "lexicon.h"

namespace com {
namespace baidu {
namespace util {
    void parse_from_file(std::string path, std::vector<std::string> types) {
        ifstream fin(path.c_str(), ifstream::in);  // open as stream
        std::string line;
        if (!fin) {
            std::cerr << "Couldn't open the file " << path << "!";
            exit(1); 
        }
        
        while (std::getline(fin, line)) {

        }

    }

    void LexiconParser::translate_builtin_datatype(std::string record) {
    }

    template<class T>
       T LexiconParser::translate_user_defined_struct(std::string record) {
    }
}
}
}

int main(int argc, char** argv) {
    com::baidu::util::LexiconParser lp;
    return 0;
}
