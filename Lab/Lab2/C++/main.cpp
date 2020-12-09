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
json get_webhooks();
void save_webhooks(json config);
std::string gen_webhook_page();
void webhooks_get(const Request& req, Response& res);
void webhooks_post(const Request& req, Response& res);
void yandex_hook(const Request& req, Response& res);
int main(){
	Server svr;
	svr.Get("/webhooks", webhooks_get);
	svr.Post("/webhooks", webhooks_post);
	svr.Post("/yandex_hook", yandex_hook);
	svr.listen("localhost", 1234);
}