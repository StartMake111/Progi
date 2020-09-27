#include <iostream>
#include <cmath>

using namespace std;

int main(){
    int k = 1, N, c=0;
    cin >>N;
    if (N > pow(10,15) or N<1){
        return 0;
    }
    for (int i = 0; i < 99999999999999; i++)
    {
        if (k <= N){
            k*=2;
            c++;
        }
        else{
            break;
        }
    }
    
    cout << c << endl;
}