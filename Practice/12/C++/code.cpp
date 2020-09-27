#include <iostream>

using namespace std;

int main(){

    int N,k = 1;
    cin >> N;

    for (int i = 1; i < N+1; i++)
    {
        k *= i;
    }
    
cout << k << endl;


return 0;
}