#include <iostream>
#include <vector>
#include <fstream>
#include <random>
using namespace std;

std::ostream& operator<< (std::ostream& print, const std::vector<int> vector){
    print << vector.size() << "\t| ";
    for (auto& i : vector) print << &i << " ";
    return print << "\n";
}

int main(){
    vector<int> vec;
    std::ofstream file;
    file.open("datawith.txt");
    cout << file.is_open();
    if (file.is_open()){
        for (int i = 0; i < 64; i++)
        {
            vec.push_back(rand());
            file << vec;
        }
        for (int i = 0; i < 64; i++){
            vec.pop_back();
            file << vec;
        }
        for (int i = 0; i < 64; i++)
        {
            vec.push_back(rand());
            file << vec;
        }
        for (int i = 0; i < 64; i++){
            vec.pop_back();
            file << vec;
        }
    }
    file.close();
}