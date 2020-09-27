#include <iostream>

using namespace std;

int main(){
    int k = 1, N, c=0;
    cin >>N;
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