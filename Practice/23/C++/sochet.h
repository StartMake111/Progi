#include <iostream>
#include "factorial.h"
using namespace std;
double C (int n, int k){
    return fact(n) / (fact(k)*fact(n-k));
}