#include "factorial.h"
#include "teylor.h"
#include "sochet.h"
#include <iostream>
#include <cmath>
#include <iomanip>
const long double pi = 3.141592653589793238462;
using namespace std;
int main(){
    // n
    cout << 'n' << "\t" << "n!" << endl;
    for (int i=1; i<11;i++) cout << i<<"\t"<<fact(i) << endl;
    
    // sin
    cout << "\n" << 'x' << "\t" << "sin(x)" << endl;
    for (double x = 0; x <= pi / 4; x += pi / 180)
    {
        cout.precision(4);
        cout << x <<"\t" << sinus(x,5) << endl;
    }
    
    // C
    cout << "\n" << 'k' << "\t" << "C(k,10)" << endl;
    for (int i = 1; i < 11; i++) cout << i <<"\t" << C(10,i) << endl;
};