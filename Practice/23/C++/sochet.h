#include <iostream>
#include "factorial.h"
using namespace std;
double C (int n, int k){
    if (k==10) return 0;
    return fact(n) / (fact(k)*fact(n-k));
}