#include <iostream>
#include <cmath>

using namespace std;

int main(){

    int N,k = 1;
    cin >> N;
    for (int i = 1; i < N+1; i++)
    {
        k *= i;
    }
if (k < 0 or k > pow(10,9)){
    return 0;
}
cout << k << endl;


return 0;
}