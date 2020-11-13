#include <iostream>

using namespace std;
int fact(int x){
    if (x > 0) return x*fact(x-1);
    else return 0;
}