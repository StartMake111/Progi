#include <iostream>
#include <cstring>
using namespace std;
string a;
int A;
int main() {
    cin >> A;
    for (int i=0; i<A; i++){
        cin >> a; 
    if (a.length() > 8 and a.length()<0){
        return 0;
    }
    if ((a[0] == 'a') and (a[4] == '5') and (a[5] == '5') and (a[6] == '6') and (a[7] == '6') and (a[8] == '1')){
        cout << a << ' ';
    }
    }

    return 0;
}