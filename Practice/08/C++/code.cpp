#include <iostream>

using namespace std;

int main(){

    double a,b,c;
    char A;

    cin >> a >> A >> c;

    if (A == '+'){
        cout << a+c << endl;
    }
    if (A == '-'){
        cout << a-c << endl;
    }
    if (A == '*'){
        cout << a*c << endl;
    }
    if (A == '/'){
        if (c==0){
            cout << "На ноль делить нельзя";
            return(0);
        }
        cout << a/c << endl;
    }
    else {
        cout << "— Ну как там с деньгами?" << endl << "— А?" << endl << "— Как с деньгами-то там?" << endl << "— Чё с деньгами?" << endl << "--Чё?" << endl << "— Куда ты звонишь?" << endl << "— Тебе звоню." << endl << "— Кому?" << endl << "— Ну тебе." << endl << "— Кому тебе?" << endl << "— А вот тебе вот." << endl;
    }

}