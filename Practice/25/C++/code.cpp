#include <vector>
#include <iostream>
#include <random>
using namespace std; 
void print(vector<int> mass){
    cout << "" << "\n";
    for (int i = 0; i < mass.size()-1; i++)
    {
        cout << mass[i] << " ";
    }
    cout << "\n";    
}
bool is_sorted(vector<int> mass, bool des = true){
    int size = mass.size();
    if (des){
        for (int i = 0; i < size; i++)
        {
            if (mass[i] > mass[i+1]) return false;
        }
    }else{
        for (int i = 0; i < size; i++)
        {
            if (mass[i] < mass[i+1]) return false;
        }
    }
    return true;
}
vector<int> Bozosort(vector<int> mass, bool des = true){
    int size = mass.size();
    vector<int> result = mass;
    while(is_sorted(result, des) == false){
        for (int i;i<size;i++){
            int k = std::rand() % size;
            int j = std::rand() % size;
            result[j], result[k] = result[k], result[j];
        }
    }
    return result;
}
vector<int> Bozosort(vector<vector<int>> mass, bool des = true){
    vector<int> result;
    for (vector<int> vec : mass){
        for(int elem : vec){
            result.push_back(elem);
        }
    }
    return Bozosort(result, des);
}
vector<int> Bozosort(int a1, int a2, int a3, bool des=true){
    vector<int> result = {a1,a2,a3};
    return Bozosort(result, des);
}
int main(){
    int n;
    cin >> n;
    vector<int> navvod;
    vector<int> stroka;
    vector<vector<int>> matrica;
    for (int i = 0; i < n; i++)
    {
        int num;
        cin >> num;
        stroka.push_back(num);
        navvod.push_back(num);
        if (i % int(sqrt(n))==0){
            matrica.push_back(stroka);
            stroka.clear();
        }
    }
    print(Bozosort(navvod));
    print(Bozosort(navvod, false));
    print(Bozosort(matrica));
    print(Bozosort(matrica, false));
    print(Bozosort(navvod[0],navvod[1],navvod[2]));
    print(Bozosort(navvod[0],navvod[1],navvod[2], false));
}