#include <iostream>
#include <cmath>

using namespace std;

int main(){
    double s,s1[2],s2[2],l1,r1,l2,r2;
    cin >> s >> l1 >> r1 >> l2 >> r2;
    s1[0] = l1; s1[1] = r1;
    s2[0] = l2; s2[1] = r2;
    if (pow(10,-15) > s,l1,r1,l2,r2 or s,l1,r1,l2,r2 > pow(10,15)) {
        return 0;
    }
    if (l1 > r1){
        return 0;
    }
    if (l2>r2){
        return 0;
    }
    if ( (s1[0] + s2[1]) == s) {
    cout << s1[0] << " " << s2[1] << endl ;
    return 0;
    }
    if ( (s1[1] + s2[0]) == s) {
    cout << s1[1] << " " << s2[0] << endl;
    return 0;
    }
    if ( (s1[0] + s2[1]) == s) {
    cout << s1[0] << " " << s2[1] << endl ;
    return 0;
    }
    if ( (s1[1] + s2[1]) == s) {
    cout << s1[1] << " " << s2[1] << endl;
    return 0;
    }
    else {
        cout << "-1" << endl;
    }
return 0;
}