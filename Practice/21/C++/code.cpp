#include <iostream>
using namespace std;

int main() {

int n, min, max, kmin, kmax, maxmax;
min = 1000000001;
max = -1;
maxmax = 0;

cin >> n;

long long b[n];
long long f[n];

for(int i = 0; i < n; i++){
cin >> b[i];
}
for(int i = 0; i < n; i++){
f[i] = 0;
}
for(int i = 0; i < n; i++){
if(b[i] > max){
max = b[i];
f[n-1] = i;
maxmax = max;
}
if(b[i] < min){
min = b[i];
f[0] = i;
}
}
for (int k=1; k < n; k++) {
    for (int j=0; j < n; j++){
        if(b[j] > min && b[j] < max){
            max = b[j];
            f[k] = j;
        }
        min = max;
        max = maxmax;
}
}
for(int i = 0; i < n; i++){
cout << f[i] << " ";
}
return 0;
}