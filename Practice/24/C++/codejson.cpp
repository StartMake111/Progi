#include <iostream>
#include <fstream>
#include "json.hpp"
#include <iomanip>
using namespace std;
using json = nlohmann::json;
int main(){
    std::ifstream input("in.json");
    std::ofstream output("out.json");
    json jin; input >> jin;
    json jout;
    for (auto& ochered : jin) 
    {
    int userID = ochered["userId"];
    bool completed = ochered["completed"];
        json obj;
        json *cheloveck = &obj;
        for (auto& ochered : jout) {
            if (ochered["userId"] == userID){
                cheloveck = &ochered;
                break;
            }
        }
        if (cheloveck -> empty()){
            jout.push_back({
            {"userId", userID},
            {"task_completed", 0}
        });
        cheloveck = &jout[jout.size()-1];
    }
    if (completed){
        (*cheloveck)["task_completed"] = static_cast<int>((*cheloveck)["task_completed"]) + 1;
    }
}

output << std::setw(2) << jout << endl;
}