#include <iostream>
#include <vector>
#include <fstream>
#include <ostream>
#include "csv.hpp"
using namespace std;

struct Passenger
{
    bool survive;
    int Pclass;
    string Name;
    string Sex;
    float Age;
    int SibSp;
    int Parch;
    string Ticket;
    float Fare;
    string Cabin;
    string Embarked;
};

std::istream& operator>> (std::istream& in, std::vector<Passenger>& passengers){
    csv::CSVReader reader("train.csv");
    float Age;
    for (auto& el : reader){
        if (el["Age"].get() == ""){
            Age = -1;
        }
        else {
            Age = el["Age"].get<float>();
        }
        Passenger passenger{
            el["Survived"].get<bool>(),
            el["Pclass"].get<int>(),
            el["Name"].get(),
            el["Sex"].get(),
            Age,
            el["SibSp"].get<int>(),
            el["Parch"].get<int>(),
            el["Ticket"].get(),
            el["Fare"].get<float>(),
            el["Cabin"].get(),
            el["Embarked"].get(),
        };
        passengers.push_back(passenger);
    }
    return in;
}
std::ostream& operator<< (std::ostream& out, std::vector<Passenger>& passengers){
    ifstream file;
    auto lenname = 0;
    auto lenticket = 0;
    auto lenFare = 0;
    auto lencabin = 0;
    file.open("output.txt");
    for (auto& pep : passengers){
        if (pep.Name.length()> lenname) {
            lenname = pep.Name.length();}
        if (pep.Ticket.length()> lenticket) {
            lenticket = pep.Ticket.length();}
        if (sizeof(pep.Fare)> lenFare) {
            lenFare = sizeof(pep.Fare);}    
        if (pep.Cabin.length()> lencabin) {
            lencabin = pep.Cabin.length();}
    }
    for (auto& pep : passengers){
        out << pep.survive << pep.Pclass << pep.Name << string(lenname - pep.Name.length(), ' ')
        << pep.Sex << pep.Age << pep.SibSp << pep.Parch << pep.Ticket << string(int(lenticket - pep.Ticket.length()), ' ')
        << pep.Fare << string(lenFare - sizeof(pep.Fare), ' ')
        << pep.Cabin << string(lencabin - pep.Cabin.length(), ' ')
        << pep.Embarked << "\n";
    }
    return out;
}
int main(){
        std::vector<Passenger> passengers;
        std::ifstream data;
        data.open("train.csv");
        if (data.is_open()) data >> passengers;
        data.close();
        ofstream data1;
        data1.open("output.txt");
        if (data.is_open()) data1 << passengers;
        data1.close();

    }