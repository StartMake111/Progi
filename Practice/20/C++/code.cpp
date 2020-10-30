#include <iostream>
#include <vector>
#include <string>

using namespace std;

int price, volue;
char name;
struct napitock{
    string name;
    long long price = 0;
    long long volue = 0;
};

int main()
{
    napitock poidet_v_sitopiano;
    napitock vvod;
    long long deneg, litrov, luche_litrov, skolko_napitkov, k = 0;
    cin >> deneg >> skolko_napitkov;
    for (int i = 0; i < skolko_napitkov; i++)
    {
        cin >> vvod.name >> vvod.price >> vvod.volue;
        litrov = (deneg/vvod.price) * vvod.volue;
        if (litrov == 0) continue;
        if (k == 0) poidet_v_sitopiano = vvod; k+=1;
        luche_litrov = (deneg/poidet_v_sitopiano.price) * poidet_v_sitopiano.volue;
        if (litrov > luche_litrov) poidet_v_sitopiano = vvod;
    }
    if (poidet_v_sitopiano.price == 0) cout << "Error" << endl;
    else 
    {
        cout << poidet_v_sitopiano.name << ' ' << deneg / poidet_v_sitopiano.price << endl; 
        cout << deneg / poidet_v_sitopiano.price * poidet_v_sitopiano.volue << endl;
        cout << deneg - poidet_v_sitopiano.price * (deneg / poidet_v_sitopiano.price) << endl;
    }
}