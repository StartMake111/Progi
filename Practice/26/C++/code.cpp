#include <vector>
#include <iostream>
#include <random>
using namespace std; 
template<class T>
void print(vector<T> mass){
    for (int i = 0; i < mass.size(); i++)
    {
        cout << mass[i] << " ";
    }
    cout << "\n";    
}
 
template<class T>
bool is_sorted(vector<T> mass, bool des = true){
    int size = mass.size();;
    if (des){
        for (int i = 0; i < size-1; i++)
        {
            if (mass[i] > mass[i+1]) return false;
        }
    }else{
        for (int i = 0; i < size-1; i++)
        {
            if (mass[i] < mass[i+1]) return false;
        }
    }
    return true;
}
template<class T>
vector<int> Bozosort(vector<T> mass, bool des = true){
    int size = mass.size();
    vector<int> result = mass;
    while(is_sorted(result, des) == false){
        for (int i=0;i<size;i++){
            int k = std::rand() % size;
            int j = std::rand() % size;
            swap(result[k],result[j]);
        }
    }
    return result;
}
template<class T>
vector<T> Bozosort(vector<vector<T>> mass, bool des = true){
    vector<T> result;
    for (vector<T> vec : mass){
        for(int elem : vec){
            result.push_back(elem);
        }
    }
    return Bozosort(result, des);
}
template<class T>
vector<T> Bozosort(T a1, T a2, T a3, bool des=true){
    vector<T> result = {a1,a2,a3};
    return Bozosort(result, des);
}
int main(){
    int n;
    cin >> n;
    vector<int> navvod;
    vector<int> stroka;
    vector<vector<int>> matrica;
    for (int i = 1; i < n+1; i++)
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
    print(Bozosort(navvod[0],navvod[1],navvod[2],false));
}