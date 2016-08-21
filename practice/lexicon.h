#include <vector>
#include <string>

namespace com {
namespace baidu {
namespace util {

class LexiconParser {
    void parse_from_file(std::string path, std::vector<std::string> types);
    void translate_builtin_datatype(std::string record);
    template<class T>
        T translate_user_defined_struct(std::string record);
};


}
}
}
