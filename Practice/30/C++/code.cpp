#include <iostream>
#include <vector>
#include <map>

struct Item;

int main(){
    std::vector<Item> LootBox;
    std::map <void, double> chance {
        {GetCoin(1000), 50},
        {GetRunefire(1), 5},
        {GetRunewater(1), 13},
        {GetRuneearth(1), 7},
        {GetRuneair(1), 14},
        {GetRunefire(5), 0.6},
        {GetRunewater(5), 1.3},
        {GetRuneearth(5), 0.7},
        {GetRuneair(5), 1.4},
        {GetRunefire(5), 0.06},
        {GetRunewater(5), 0.13},
        {GetRuneearth(5), 0.07},
        {GetRuneair(5), 0.14},
    };
}






struct Weapon
{
    uint damage;
    uint ctitical;
    uint durability;
};
struct Armor
{
    uint guard;
    uint durability;
};
struct Coin
{
    uint count;
};
struct Rune
{
    int level;
    enum class Element{
        FIRE,
        WATER,
        EARTH,
        AIR,
    } element;
};
struct Item
{
    enum class ItemType{
        COIN,
        RUNE,
        WEAPON,
        ARMOR,
    } type;
    union Value
    {
        Coin coin;
        Rune rune;
        Weapon weapon;
        Armor armor;
    } value;
    Item& operator++ (){;
    }  
};