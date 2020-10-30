#include <iostream>
#include <vector>
#include <algorithm>
#include <iterator>
using namespace std;
const string maze[] = {
    "####B######################",
    "# #           #      #    #",
    "# # # ###### #### ####### #",
    "# # # #       #   #       #",
    "#   # # ######### # ##### #",
    "# # # #   #       #     # #",
    "### ### ### ############# #",
    "# #   #     # #           #",
    "# # #   ####### ###########",
    "# # # #       # #         C",
    "# # ##### ### # # ####### #",
    "# # #     ### # #       # #",
    "#   ##### ### # ######### #",
    "######### ### #           #",
    "# ####### ### #############",
    "A           #   # #   #   #",
    "# ############# # # # # # #",
    "# ###       # # # # # # # #",
    "# ######### # # ### # # # F",
    "#       ### # #     # # # #",
    "# ######### # ##### # # # #",
    "# #######   #       #   # #",
    "# ####### ######### #######",
    "#         #########       #",
    "#######E############D######"
};
int lenght = 1;
void schetchick(int k=0){
    k += 1;
}
vector<pair<int,int>> posesh;
void put(int x, int y){
    if (find(posesh.begin(), posesh.end(), make_pair(x,y)) != posesh.end()) return;
    else posesh.push_back(make_pair(x, y));
    if (x >= sizeof(maze[0]) or y >= sizeof(maze) or x < 0 or y < 0) return;
    if (maze[x][y-1] == ' ') put(x, y - 1);
    if (maze[x-1][y] == ' ') put(x - 1, y);
    if (maze[x+1][y] == ' ') put(x + 1, y);
    if (maze[x][y+1] == ' ') put(x, y + 1);
    if (maze[x][y - 1] != ' ' and maze[x][y - 1] != '#') cout << maze[x][y-1] << endl; schetchick(); return;
    if (maze[x - 1][y] != ' ' and maze[x - 1][y] != '#') cout << maze[x-1][y] << endl; schetchick(); return;
    if (maze[x + 1][y] != ' ' and maze[x + 1][y] != '#') cout << maze[x+1][y] << endl; schetchick(); return;
    if (maze[x][y + 1] != ' ' and maze[x][y + 1] != '#') cout << maze[x][y+1] << endl; schetchick(); return;
}
int main(){
    int x,y;
    cin >> x >> y;
    put(x,y);
}