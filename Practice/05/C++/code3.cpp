#include <iostream>

using namespace std;


int main(){


    double g=9.8, v, t ,Xt, x0;

    cout << "Vvedi koordinatu, skorost, vremya cheres probel : "; cin >> x0 >> v >> t;

    Xt = x0+ v*t - ((g*t*t)/2);

    cout << abs(Xt-x0) << endl;

    return 0;


}
