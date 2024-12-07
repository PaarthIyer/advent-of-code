#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <chrono>

using namespace std;

void read_file(const string &filename, vector<long long int> &targets, vector<vector<int>> &nums)
{
    ifstream inFile(filename);

    for (string line; getline(inFile, line);)
    {
        int colon = line.find(':');

        long long int target = stoll(line.substr(0, colon));

        vector<int> numList;
        string num;
        stringstream ss(line.substr(colon + 2));
        while (getline(ss, num, ' '))
        {
            numList.push_back(stoi(num));
        }

        targets.push_back(target);
        nums.push_back(numList);
    }

    inFile.close();
}

bool valid_ops_runner(long long target, const vector<int> &nums, int index)
{
    if (index == 0)
        return target == nums[0];

    if (target % nums[index] == 0 && valid_ops_runner(target / nums[index], nums, index - 1))
        return true;

    if (target > nums[index] && valid_ops_runner(target - nums[index], nums, index - 1))
        return true;

    return false;
}

bool valid_ops(long long target, const vector<int> &nums)
{
    int len = nums.size();
    return valid_ops_runner(target, nums, len - 1);
}

int main()
{

    auto start = chrono::high_resolution_clock::now();
    string filename = "input.in";

    long long int target;
    vector<int> nums;

    long long int answer = 0;

    string num;
    int colon;

    ifstream inFile(filename);
    for (string line; getline(inFile, line);)
    {
        colon = line.find(':');
        target = stoll(line.substr(0, colon));

        stringstream ss(line.substr(colon + 2));
        while (getline(ss, num, ' '))
        {
            nums.push_back(stoi(num));
        }

        if (valid_ops(target, nums))
        {
            answer += target;
        }
        nums = {};
    }

    inFile.close();

    auto end = chrono::high_resolution_clock::now();
    auto duration = chrono::duration_cast<chrono::nanoseconds>(end - start);

    cout << "Time taken to execute: " << duration.count() / 1000 << " us" << endl;
    cout << "Answer: " << answer << endl;

    return 0;
}