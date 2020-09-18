#include <iostream>

using namespace std;

int main()
{

    int a, b, d;

    d = a, a = b, b = d;
    cout << a << endl << b << endl;
    
    a = a+b;
    b = a-b;
    a = a-b;

    cout << a << endl << b << endl;



    return 0;
}