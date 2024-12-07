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
        stringstream ss(line);
        string targetStr;
        getline(ss, targetStr, ':');

        long long int target;
        target = stoll(targetStr);

        vector<int> numList;
        int num;
        while (ss >> num)
        {
            numList.push_back(num);
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
    vector<long long int> targets;
    vector<vector<int>> nums;
    long long int answer = 0;

    read_file(filename, targets, nums);

    for (int i = 0; i < targets.size(); ++i)
    {
        if (valid_ops(targets[i], nums[i]))
            answer += targets[i];
    }

    auto end = chrono::high_resolution_clock::now();
    auto duration = chrono::duration_cast<chrono::nanoseconds>(end - start);

    cout << "Time taken to execute: " << duration.count() / 1000 << " us" << endl;
    cout << "Answer: " << answer << endl;

    return 0;
}