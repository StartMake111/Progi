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

std::istream &operator>>(std::istream &in, std::vector<Passenger> &passengers)
{
    csv::CSVReader reader("train.csv");
    float Age;
    for (auto &el : reader)
    {
        if (el["Age"].get() == "")
        {
            Age = -1;
        }
        else
        {
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
std::ostream &operator<<(std::ostream &o, std::vector<Passenger> &passengers)
{
    auto writer = csv::make_csv_writer(o);

    writer << std::vector<std::string>{
        "Survived", "Pclass", "Name", "Sex", "Age", "SibSp", "Parch", "Ticket", "Fare", "Cabin", "Embarked"};

    for (auto &pass : passengers)
    {
        writer << std::make_tuple(
            pass.survive,
            pass.Pclass,
            pass.Name,
            pass.Sex,
            pass.Age,
            pass.SibSp,
            pass.Parch,
            pass.Ticket,
            pass.Fare,
            pass.Cabin,
            pass.Embarked);
    }

    return o;
}
int main()
{
    std::vector<Passenger> passengers;

    std::ifstream data("train.csv");
    data >> passengers;

    sort(passengers.begin(), passengers.end(), [&](Passenger a, Passenger b) { return a.Age < b.Age; });

    std::vector<Passenger> onlyFemale;
    for (auto &pass : passengers)
    {
        if (pass.Sex == "female" && pass.Pclass == 1)
        {
            onlyFemale.push_back(pass);
        }
    }
    std::ofstream output("output.csv");
    output << onlyFemale;

    return 0;
}