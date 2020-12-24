#include <iostream>
#include <iomanip>
#include <fstream>
#include <string>
#include <ctime>
#include "Include/nlohman/json.hpp"
#include "Include/cpp-httplib/httplib.h"
using json = nlohmann::json;
using namespace httplib;
json get_json();
json get_cache();
json get_hourly_request(json &hourly);
bool cachejson(json ca);
json get_time();
void findandreplace(std::string &data, std::string toSearch, std::string replaceStr){
    size_t pos = data.find(toSearch);
    while(pos != std::string::npos){
        data.replace(pos, toSearch.size(), replaceStr);
        pos = data.find(toSearch, pos + replaceStr.size());
    }
}
void responce(const Request &req, Response &res){
    json body1;
    json prognoz1;
    body1 = get_cache();
    if (body1.empty()) {
        body1 = get_json();
        if (body1.contains("err")) {
            res.set_content(body1["err"], "text/plain");
        }
        else if (body1.contains("err")) {
            res.set_content(body1, "text/json");
        }
        cachejson(body1);
    }
        prognoz1 = get_hourly_request(body1["hourly"]);
        if (prognoz1.contains("err")) {
            res.set_content(prognoz1["err"], "text/plain");
            return;
        }
    std::string tamplname = "templ.html";
    std::ifstream tamplate(tamplname);
    std::string str;
    if (tamplate.is_open()){
        getline(tamplate,str, '\0');
        tamplate.close();
    }
    else {
        res.set_content("Error", "text/plain");
        return;
    }
    findandreplace(str, "{hourly[i].weather[0].description}", prognoz1["weather"][0]["description"]);
    findandreplace(str, "{hourly[i].weather[0].icon}", prognoz1["weather"][0]["icon"]);
    findandreplace(str, "{hourly[i].temp}", std::to_string(int(round(prognoz1["temp"].get<double>()))));
    res.set_content(str, "text/html");
}
void responceraw(const Request &req, Response &res){
    json body2;
    json prognoz2;
    body2 = get_cache();
    if (body2.empty()){
        body2 = get_json();
        if (body2 == "err") {
            res.set_content(body2, "text/json");
        }
    } else if (body2.contains("err")) {
        res.set_content(body2, "text/json");
    }
    prognoz2 = get_hourly_request(body2["hourly"]);
    if (prognoz2.contains("err")) {
            res.set_content(prognoz2["err"], "text/plain");
            return;
        }
    cachejson(body2);
    json out;
    out["temp"] = prognoz2["temp"];
    out["description"] = prognoz2["weather"][0]["description"];
    res.set_content(out.dump(), "text/json");
    }
int main(){
    Server bers;
    bers.Get("/", responce);
    bers.Get("/raw", responceraw);
    bers.listen("localhost", 1234);
}