#include <iostream>
#include <vector>

using namespace std;

std::vector<int> selection_sort(std::vector<int> arr)
{
    int n = arr.size();
    for (int i = 0; i < n; i++)
    {
        for (int j = i; j < n; j++)
        {
            if (arr[i] > arr[j])
            {
                std::swap(arr[i], arr[j]);
            };
        };
    };
    return arr;
}

int main()
{
    std::vector<int> arr = {10, 9, 8, 7, 6, 5, 4, 3, 2, 1};
    std::vector<int> sorted_arr = selection_sort(arr);

    for (int num : sorted_arr)
    {
        cout << num << endl;
    };

    return 0;
}