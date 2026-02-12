#include <iostream>
#include <vector>

using namespace std;

std::vector<int> bubble_sort(std::vector<int> arr)
{
    int n = arr.size();

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n - i - 1; j++)
        {
            if (arr[j] > arr[j + 1])
            {
                std::swap(arr[j], arr[j + 1]);
            }
        }
    }
    return arr;
}

std::vector<int> main()
{
    std::vector<int> arr;
    bubble_sort(arr);
}