#include <iostream>
#include <iomanip>
#include <fstream>
#include <string>
#include <ctime>
#include "Include/cpp-httplib/httplib.h"
#include "Include/nlohman/json.hpp"
#include "main.cpp"
using json = nlohmann::json;
using namespace httplib;
void findandreplace(std::string & data, std::string toSearch, std::string replaceStr){
    size_t pos = data.find(toSearch);
    while(pos != std::string::npos){
        data.replace(pos, toSearch.size(), replaceStr);
        pos = data.find(toSearch, pos + replaceStr.size());
    }
}
void responce(const Request &req, Response *res){
    json body;
    json prognoz;
    body = get_cache();
    if (body.empty()){
        prognoz = get_hourly_request(body["hourly"]);
        if (!prognoz["err"].is_null()){
            return;
        }
    }
    string tamplname = "templ.html";
    ifstream tamplate(tamplname);
    string str;
    if (tamplate.is_open()){
        getline(tamplate,str, '\0');
        tamplate.close();
    }
    else {
        return;
    }
    findandreplace(str, "{hourly[i].weather[0].description}", prognoz["weather"][0]["description"]);
    findandreplace(str, "{hourly[i].weather[0].icon}", prognoz["weather"][0]["icon"]);
    findandreplace(str, "{hourly[i].temp}", to_string(int(round(prognoz["temp"].get<double>()))));
}
void responceraw(const Request &req, Response *res){
    json body;
    json prognoz;
    body = get_cache();
    if (body.empty()){
        
    }
}