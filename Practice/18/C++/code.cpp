#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main()
{
	string slovo;
	cin >> slovo;
	double bukvi[26] = {};
	double chanse_proiznesti = 1;
	char slovar[26] = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'x'};
	vector<string> s1 = {"hallo", "klempner", "das", "ist", "fantastisch", "fluggegecheimen"};
	int dlinna = 0;

	for (int i = 0; i < s1.size(); i++) {
		for (int j = 0; j < s1[i].size(); j++) {
			dlinna++;
			for (int k = 0; k < 26; k++) {
				if (s1[i][j] == slovar[k])
                {
                    bukvi[k]++;
                }
			}
		}
	}

	for (int i = 0; i < 26; i++) 
    {
        bukvi[i] = bukvi[i] / dlinna;
    }

	for (int i = 0; i < slovo.size(); i++) {
		for (int j = 0; j < 26; j++) {
			if (slovo[i] == slovar[j]){
                chanse_proiznesti = chanse_proiznesti * bukvi[j];
		}
        }
	}
	cout.precision(16);
	cout << chanse_proiznesti << endl;
return(0);
}