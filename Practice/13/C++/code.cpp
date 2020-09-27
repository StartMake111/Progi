#include <iostream>
#include <math.h>
using namespace std;
int main(){
    int a,k=0;
    cin>>a;
    if (a>pow(10,9) or a<1){
        return 0;
    }
if ((a==1) or (a==0) or (a > pow(10, 9))){
    return 0;
}
    for (int i = 2; i < 10; i++)
    {
        if (a%i==0){
            k++;
        }
    }
if (k>1){
    cout << "Составное" << endl;
}
else{
    cout << "Простое" << endl;
}
}