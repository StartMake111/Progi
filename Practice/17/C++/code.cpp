#include <iostream>
#include "list"
#include "string"

using namespace std;

long long a=1,b,Max=0,black=0,red=0,MasMax=-1;
int d[37];
int main(){
    while (a > 0){
    cin >> a;
    if (a > 36){
        return 0;
    }
    d[a] += 1;
    if (a == 1 or a ==3 or a == 5 or a ==7 or a == 9 or a == 12 or a == 14 or a == 16 or a == 18 or a == 19 or a == 21 or a == 23 or a == 25 or a == 27 or a == 30 or a ==32 or a == 34 or a == 36) red++; else black++;
    for (int i = 0; i < 37; i++)
    {
        if (d[i]>Max){
            Max = d[i];
        }
    }
    for (int i = 0; i < 37; i++)
    {
        MasMax++;
        if (d[i] == Max){
            cout << MasMax << ' ';
        }
    }
    MasMax = -1;
    cout << endl;

    for (int i = 0; i <= 36; i++){
        cout << ((a==i)? 0 : i) << ' ';
    }
    cout << endl << red << ' ' << black << endl;
}
}