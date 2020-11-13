#include </home/startmake/Рабочий стол/Programming/Practice/23/C++/factorial.cpp>
#include <iostream>
using namespace std;
int main(){
    int x;
    cin >> x;
    for (int i; i<x+1;i++) cout << i<<"\t"<<fact(i) << endl;
}