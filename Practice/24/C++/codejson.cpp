#include <iostream>
#include <fstream>
#include "json.hpp"
#include <vector>
#include <iomanip>
using namespace std;
using json = nlohmann::json;
int main(){
    std::ifstream input("in.json");
    json j; input >> j;
    json o;
    std:ofstream output("out.json");
    cout << j;
    
}