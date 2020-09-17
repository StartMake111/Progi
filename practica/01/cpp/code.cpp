#include <iostream>

using namespace std;

int main()
{
    cout << "Resultat virasenia 2+2*2 = " << 2+2*2 << endl;

    int a = 3,b = 3.14, d;
    double a1 = 3, b1 = 3.14;
    
    cout << a << endl << b << endl << a1 << endl  << b1 << endl;

    cin >> a, b, a1, b1;
    cout << a+b << endl << a-b << endl << a*b << endl << a/b;
    cout << a1+b1 << endl << a1-b1 << endl << a1*b1 << endl << a1/b1;
    cout << a1+b << endl << a1-b << endl << a1*b << endl << a1/b;
    cout << a+b1 << endl << a-b1 << endl << a*b1 << endl << a/b1;

    d = a, a = b, b = d;
    cout << a << endl << b << endl;
    
    a = a+b;
    b = a-b;
    a = a-b;

    cout << a << endl << b << endl;

    double g=9.8, v, t ,S, x0;

    cout << "Vvedi koordinatu, skorost, vremya cheres probel : "; cin >> x0 >> v >> t;

    S = x0+ v*t - ((g*t*t)/2);

    cout << S << endl;

    //cout << a << endl << b << endl;
    return 0;
}