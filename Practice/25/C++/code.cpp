#include <vector>
#include <iostream>
#include <random>
using namespace std; 
bool is_sorted(vector<int> mass, bool des = true){
    int n = sizeof(mass);
    if (des){
        for (int i = 0; i < n; i++)
        {
            if (mass[i] > mass[i+1]) return false;
        }
    }else{
        for (int i = 0; i < n; i++)
        {
            if (mass[i] < mass[i+1]) return false;
        }
    }
    return true;
}
vector<int> Bozosort(vector<int> mass, bool des = true){
    int n = sizeof(mass);
    while(is_sorted(mass, des) == false){
        for (int i;i<n;i++){
            int k, j = rand(), rand(n-1);
            mass[j], mass[k] = mass[k], mass[j];
        }
    return mass;
    }
}
void Print(vector<int> mass){

}