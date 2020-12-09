#include <iostream>
#include <fstream>
#include <vector>
#include <filesystem>

#include "Include/cpp-httplib/httplib.h"
#include "Include/nlohman/json.hpp"

using json = nlohmann::json;
using namespace httplib;
namespace fs = std::filesystem;

void replace_all(std::string& data,
	const std::string& to_replace,
	const std::string& replace_with)
{
	size_t pos = data.find(to_replace);
	while (pos != std::string::npos)
	{
		data.replace(pos, to_replace.size(), replace_with);
		pos = data.find(to_replace, pos + replace_with.size());
	}
}
void gen_responceMute(const Request& req, Response& res){
	std::cout << req.body.c_str();
	std::string str= u8R"(
		{
			"response":{
					"text": "Здравствуйте! Я помогу вас с покупками.",
					"tts":"Здр-авствуйте! Я помогу вас с пок-упками.",
        ],
        "end_session": false
      },
      "version": "1.0"
    })";
	res.set_content(str, "text/json; charset=UTF-8");