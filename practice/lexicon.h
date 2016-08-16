#include <vector>
typedef std::string Str;

namespace com {
namespace baidu {
namespace utility {

    struct LexiconTable {
        int col_num;
    };

    void parse_from_file(std::string path);
    void parse_from_file(std::ifstream f);
}
}
}
