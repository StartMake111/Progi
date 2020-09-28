#include <iostream>
#include <cmath>


using namespace std;

int main(){

    double a,b,c,p,S,s,x1,x2,x3,y1,y2,y3;

    cout << "Viberi sposob resheniya. 1 cherez storoni, 2 cherez koordinati : ";
    cin >> a;

    if (a==1){
        cout << "Vvedi storoni treugolnika cherez probel : ";
        cin >> a >> b >> c;
        if (a==0 or b==0 or c==0 or a + b > c or a+c>b or c+b > a){
            cout << "Это не треугольник" << endl;
            return 0;
        }
        if (a < 0 or b < 0 or c < 0){
            cout << "Ошибкааааа, не бывает отрицательной длинны" << endl;
            return 0;
        }
        p = (a+b+c)/2;
        S = sqrt(p*(p-a)*(p-b)*(p-c));
        cout << "S = " << S << endl;
    } 

    if (a==2){
        cout << "Vvedi koordinati vershin treugolnika cherez probel v kazdoi stroke" << endl;
        cin >> x1 >> y1;
        cin >> x2 >> y2;
        cin >> x3 >> y3;
        if (x1 == x2 and y1 == y2 or x2 == x3 and y2 == y3 or x1 == x3 and x1 == x3){
            cout << "Ошибка, нет треугольника." << endl;
            return 0;
        }
        S = abs((x2-x1)*(y3-y1)-(x3-x1)*(y2-y1))/2;
        cout << "S = " << S << endl;
    }

return 0;
}