#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;
int main(){
    cout << "Здоровеньки булы" << endl;
    int N, a=0, p;
    srand(time(NULL));
    int A = rand() %101;
while (true){
    cin >> N;
    if (N > A) {
        cout <<("Загаданное число меньше") << endl;
        a+=1;
    }
    else {
        cout <<("Загаданное число больше") << endl;
        a+=1;
    }
    if (A == N){
        cout <<("Поздравляю! Вы угадали\nХотите начаит сначала(1 - Да)") << endl;
        cin >> p;
        if (p == 1){
        a = 0;
        A = rand()%101;
                    }   
        else{
            return(0);
        }
                }
    if (a == 5){
        cout << "Вы не угадали\n Загаданное число: " << A << endl << "Хотите начаит сначала(1 - Да)"<< endl;
        cin >> p;
        if (p == 1){
                a = 0;
                A = rand()%101;
                   }
        else{
            return(0);
            }
    }
    
}
}
