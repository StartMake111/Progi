#pragma once
#include <iostream>

using namespace std;
int fact(double x){
    if (x < 1) return 1;
    else return x*fact(x-1);
}