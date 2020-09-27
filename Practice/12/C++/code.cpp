#include <iostream>
#include <cmath>

using namespace std;

int main(){

    int N,k = 1;
    cin >> N;
    if (N < 0 or N > pow(10,9)){
        return 0;
    }
    for (int i = 1; i < N+1; i++)
    {
        k *= i;
    }
    
cout << k << endl;


return 0;
}