#include <iostream>
#include <cmath>

using namespace std;


double BMI(double weight, double height){
    return weight / pow(height/100, 2);
}
void printBMI(double BMI){
    if (BMI < 18.5) cout << "Underweight" << endl;
    else if (BMI < 25) cout << "Normal" << endl;
    else if (BMI < 30) cout << "Overweight" << endl;
    else cout << "Obesity" << endl;
}
int main()
{
    do
    return 0;
}
