#include <iostream>
#include "Include/nlohman/json.hpp"
#include "Include/cpp-httplib/httplib.h"
#include <iomanip>
#include <string>
#include <ctime>
#include <fstream>
using json = nlohmann::json;
using namespace httplib;
using namespace std;
json cache;
Client cli("http://api.openweathermap.org");
Client timez("http://worldtimeapi.org");

json get_json(){
  auto res = cli.Get("/data/2.5/onecall?lat=44.9698623&lon=34.1329217&exclude=current,minutely,daily,alerts&units=metric&lang=ru&appid=e1f4f9f81642622cc21d70a6baf981e5");
  if (!res){
    return ("Err");
  }
  int status = res->status;
  if (status <200 or status >=300){
    return ("Err");
  }
  return json::parse(res->body);
}
json get_cache(){
  json cache;
  std::ifstream cachename("cache.json");
  if (cachename.is_open()){
    string inform;
    getline(cachename, inform, '\0');

    if (!inform.empty()){
      cache = json::parse(inform);
    }
    cachename.close();
  }
  else{
    return ("Err");
  }
  return cache;
}
bool cachejson(json ca){
  cache = ca;
  ofstream cachename("cache.json");
  if (cachename.is_open()){
    cachename << ca.dump(4);
    cachename.close();
  }
  else return false;
  return true;
}
json get_time(){
  auto time = timez.Get("/api/timezone/Europe/Simferopol");
  if (!time){
    return("Err");
    return json::object();
  }
  int status = time->status;
  if (status < 200 or status >= 300){
    return ("Err");
  }
  return json::parse(time->body);
} 
json get_hourly_request(json &hourly){
  json hourly_request;
  int last = hourly.size()-1;
  json timenow = get_time();
  int currtime = timenow["unixtime"];
  if (hourly[last]["dt"] <= currtime){
    return json::object();
  }
  for (int i = 0; i <= last; ++i) {
      if (hourly[i]["dt"] > currtime) {
          hourly_request = hourly[i];
          return hourly_request;
      }
  }
}