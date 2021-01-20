#include <iostream>
#include <vector>
#include <fstream>
#include <algorithm>
#include <ostream>
using namespace std;
std::string ReplaceAll(std::string str, const std::string &from, const std::string &to)
{
    size_t start_pos = 0;
    //Меняет в первой строке все совпадения второго параметра на все совпадения третьего параметра.
    while ((start_pos = str.find(from, start_pos)) != std::string::npos)
    {
        str.replace(start_pos, from.length(), to);
        start_pos += to.length();
    }
    return str;
}
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
std::vector<std::vector<std::string>> parse_cvs(
    std::istream &out,
    char end_ch = '\r',
    char quote_ch = '"',
    char sep_ch = ',')
{
    std::string line;
    std::string buffer;

    std::vector<std::string> seperated_string;
    std::vector<std::vector<std::string>> result;

    char quote_depth = 0;
    char pos = 0;

    while (std::getline(out, line, end_ch))
    {
        pos = 0;
        quote_depth = 0;

        for (char ch : line)
        {
            if (ch == sep_ch)
            {
                switch (quote_depth)
                {
                case 0:
                    seperated_string.push_back(buffer);
                    buffer.clear();
                    ++pos;
                    continue;
                case 2:
                    seperated_string.push_back(buffer);
                    buffer.clear();
                    quote_depth = 0;
                    ++pos;
                    continue;
                }
            }
            if (ch == quote_ch)
            {
                switch (quote_depth)
                {
                case 0:
                    quote_depth = 1;
                    continue;
                case 1:
                    quote_depth = 2;
                    continue;
                case 2:
                    buffer.push_back(quote_ch);
                    quote_depth = 1;
                    continue;
                }
            }
            buffer.push_back(ch);
        }
        seperated_string.push_back(buffer);
        buffer.clear();

        result.push_back(seperated_string);
        seperated_string.clear();
    }
    return result;
}
std::istream &operator>>(std::istream &in, std::vector<Passenger> &passengers)
{
    auto matrix = parse_cvs(in);
    matrix.erase(matrix.begin());

    for (auto row : matrix)
    {
        Passenger p;
        p.survive = std::stoi(row[1]);
        p.Pclass = std::stoi(row[2]);
        p.Name = row[3];
        p.Sex = row[4];
        p.Age = row[5] == "" ? 0 : std::stof(row[5]);
        p.SibSp = std::stoi(row[6]);
        p.Parch = std::stoi(row[7]);
        p.Ticket = row[8];
        p.Fare = std::stof(row[9]);
        p.Cabin = row[10];
        p.Embarked = row[11][0];

        passengers.push_back(p);
    }
    return in;
}
std::ostream &operator<<(std::ostream &stream, std::vector<Passenger> &vec)
{
    char sep = ',';
    char end = '\r';
    for (auto &pass : vec)
    {
        std::string name = pass.Name;
        name = ReplaceAll(name, "\"", "\"\"");

        stream << pass.survive << sep
               << int(pass.Pclass) << sep
               << '"' << name << '"' << sep
               << pass.Sex << sep
               << int(pass.Age) << sep
               << int(pass.SibSp) << sep
               << int(pass.Parch) << sep
               << pass.Ticket << sep
               << pass.Fare << sep
               << pass.Cabin << sep
               << pass.Embarked
               << end << std::flush;
    }
    return stream;
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
        if (pass.Sex == "female" and pass.Pclass == 1)
        {
            onlyFemale.push_back(pass);
        }
    }
    std::ofstream output("output.csv");
    output << onlyFemale;

    return 0;
}