#include <iostream>
#include <list>
#include <cmath>
#include <vector>
#include <string>
using namespace std;

int main(){
  int dlinna;
  string slovo;
  list<char> slovolist;
  vector<int> kombi;
  list<char> result;
  int el_el;
  vector<string> res;
  int i = 0;
  int len = sizeof(slovo);
  for (char c: slovo) slovolist.push_back(c);
  for (int i = 0; i < pow(sizeof(slovo), dlinna);i++) kombi.push_back(i);
  
  while (i < len){
    el_el = kombi[i];
  }



}