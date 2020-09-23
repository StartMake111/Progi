#include <iostream>

using namespace std;

int main()
{

    int a, b, d;

    cin >> a >> b;

    d = a, a = b, b = d;
    cout << a << ' '<< b << endl;
    
    swap (a, b);   


    cout << a << ' ' << b << endl;



    return 0;
}