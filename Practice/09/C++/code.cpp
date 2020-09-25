#include <iostream>
#include <string>

using namespace std;

int main(){
    int H,T,H1,T1,H2,T2,H3;
    char A;

    cin >>H>>A>>T;
    cin >>H2>>A>>T2;
    if (H>24 or H < 1){
        return 0;
    }
    if (T>60 or T <0){
        return 0;
    }

    H1 = 60*H;
    T1 = H1 + T;   
    H3 = 60*H2;
    T2 = H3 + T2;

    if (abs(T1-T2) > 15 and abs(T1-T2) < 1){
        cout << "Встреча не состоится" << endl;
        return 0;
    }

    if (abs(T1-T2) < 16 and abs(T1-T2) > 0){
        cout << "Встреча состоится" << endl;
        return 0;
    }
return 0;
}