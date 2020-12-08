#include <iostream>
#include <fstream>
#include <vector>
#include <filesystem>

#include "Include/cpp-httplib/httplib.h"
#include "Include/nlohman/json.hpp"

using json = nlohmann::json;
using namespace httplib;
namespace fs = std::filesystem;

json get_webhooks();
void gen_responceMute(const Request& req, Response& res);
void save_webhooks(json config);
std::string gen_webhook_page();
void webhooks_get(const Request& req, Response& res);
void webhooks_post(const Request& req, Response& res);
int main()
{
	Server srv;
    srv.Post("/", gen_responceMute);
	srv.Get("/webhooks", webhooks_get);
	srv.Post("/webhooks", webhooks_post);
	std::cout << "Сервер успешно запустился!\n"
		<< "Сервер откыт по адресу localhost:1234\n\n"
		<< "Откройте http://localhost:1234/webhooks в веб-браузере, "
		<< "чтобы получить доступ к панели управления веб-хуками.\n"
		<< std::endl;   
	srv.listen("localhost", 1234);
}