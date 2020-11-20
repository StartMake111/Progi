#include <iostream>
#include "Include/cpp-httplib/httplib.h"
#include "Include/nlohman/json.hpp"
#include <iomanip>
#include <string>
#include <ctime>
#include <fstream>
using json = nlohmann::json;
using namespace httplib;

int main(){
  json hour;
  json time;
  json cache;
  json body;

  Client cli("http://api.openweathermap.org");

  auto res = cli.Get("/data/2.5/onecall?lat=44.9698623&lon=34.1329217&exclude=hourly,minutely,daily,alerts&units=metric&lang=ru&appid=e1f4f9f81642622cc21d70a6baf981e5");
  if (cache.empty()){
    body = cache;  
  }
  if (res) {

    if (res->status == 200) {
      std::cout << res->body << std::endl;
      auto str = res->body;
      body = json::parse(str);
      int size = body["hourly"].size();
      int time = std::time(0);
      for (int i = 0; i < size-1; ++i)
      {
        if (body["hourly"][i]["dt"] >= time){
          hour = body["hourly"][i];
          break;
        } 
      }     
      

    }else{

      std::cout << "Status code: " << res->status << std::endl;

    }

  }

  else {

    auto err = res.error();

    std::cout << "Error code: " << err << std::endl;  

  }

}