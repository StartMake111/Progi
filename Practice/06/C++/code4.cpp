#include <iostream>
#include <cmath>

using namespace std;


int main() {

    int a,b,c;
    double D, x1, x2, x;


    cin >> a >> b >> c;
    
    
    D = b*b - (4*a*c);

    if (D < 0){

        cout << "Kak tack?" << endl;
        return 0;

    }

    if ( a == 0 ) {

        x = -c/b;

        cout << "x = " << x;

        return 0;
    }

    else {
        


    if (D == 0) {

        x = -b/(2*a);

        cout << "x =" << x << endl;

        return 0;

    }
    
    else {

        x1 = (-b - sqrt(D)) / (2 * a);

        x2 = (-b + sqrt(D)) / (2 * a);


        if (x1==x2){

            cout << "x = " << x1 << endl;

            return 0;

        }
        else {
        cout << "x1 = " << x1 << endl << "x2 = " << x2 << endl;

        }
    }
    }
}