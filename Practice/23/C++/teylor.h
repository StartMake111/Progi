#include<iostream>
#include<cmath>
#include<factorial.h>

using namespace std;

int sinus(double x, int k){
    if (x>0){
    double otv = 0;
    for (int i = 0; i < k; i++){
        otv = pow(-1, i) * pow(x, 2*i+1) / fact(2 * x +1);
    }
}
}