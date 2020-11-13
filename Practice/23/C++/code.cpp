#include <factorial.h>
#include <iostream>
#include <teylor.h>
#include <cmath>
#include <iomanip>
const long double pi = 3.141592653589793238462;
using namespace std;
int main(){
    int x;
    cin >> x;
    for (int i=1; i<x+1;i++) cout << i<<"\t"<<fact(i) << endl;
    for (double x = 0; x <= pi / 4; x += pi/180) std::setprecision(4); cout << x <<"\t" << sinus(x,5) << endl;
}