#include <iostream>
#include <cstdio>
#include <math.h>

using namespace std;

int main(){

    int a, st, b;
    cin >> a;
    cin >> st;
    b = a;
    for (int i = 0; i < st-1; i++)
    {
        a *= b;
    }
    
cout << a << endl;

return 0;
}