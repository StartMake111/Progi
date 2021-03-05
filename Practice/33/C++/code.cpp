#include <iostream>
int *create(int len, int first = 0, int toplus = 0)
{
    int *arr = new int[len];
    for (int i = 0; i < len; i++)
    {
        arr[i] = first;
        first += toplus;
    }
    return arr;
}
void shift(int *arr, int i){
    int gara;
	for(gara = *i; i > arr && *(i-1) > gara; i--) {
		*i = *(i-1);
	}
	*i = gara;
}
int *sort(int *arr, int len)
{
    int *i, *last = arr + len;
    int ival;
    for (i = arr + 1; i < last; i++)
    {
        if (*i < *(i - 1))
        {
            shift(arr,i);
        }
    }

    return arr;
}
int *print(int *arr, int len)
{
    if (len == 0)
        std::cout << "[]\n";
    std::cout << "[" << arr[0];
    for (int i = 1; i < len; i++)
    {
        std::cout << ',' << arr[i];
    }
    std::cout << "]\n";
    return arr;
}
int main()
{
    int len, first, toplus;
    std::cout << "Введите длинну, первйы элемент и шаг прогрессии";
    std::cin >> len;
    std::cin >> first;
    std::cin >> toplus;
    int *arr = create(len, first, toplus);
    sort(arr, len);
    print(arr, len);
}
