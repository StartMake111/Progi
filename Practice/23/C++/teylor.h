#ifndef GARBAGE
#define GARBAGE
#include<iostream>
#include<cmath>
#include "factorial.h"
using namespace std;
int sinus(double x, double k){
    double otvet = 0;
    for (int i; i < k; i++) otvet+= pow(-1, i) * (pow(x, 2*i+1)/ (fact(2*i+1)));
    return otvet; 
}
#endif