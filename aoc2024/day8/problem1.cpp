#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <chrono>
#include <map>
#include <set>
#include <utility>

using namespace std;

///////////////////////////////////////////////////////////////////////////

pair<int, int> operator+(const pair<int, int> &p1, const pair<int, int> &p2)
{
    return {p1.first + p2.first, p1.second + p2.second};
}

pair<int, int> operator-(const pair<int, int> &p1, const pair<int, int> &p2)
{
    return {p1.first - p2.first, p1.second - p2.second};
}

pair<int, int> operator*(const pair<int, int> &p, int scalar)
{
    return {p.first * scalar, p.second * scalar};
}

bool in_bounds(pair<int, int> p, int rowmax, int colmax)
{
    return (p.first >= 0 && p.first < rowmax && p.second >= 0 && p.second < colmax);
}
///////////////////////////////////////////////////////////////////////////

void get_anti_nodes(set<pair<int, int>> &antinodes,
                    const vector<pair<int, int>> &nodes,
                    int rowmax, int colmax)
{
    pair<int, int> temp1, temp2;
    for (int i = 0; i < nodes.size(); i++)
    {
        for (int j = i + 1; j < nodes.size(); j++)
        {
            temp1 = (nodes[i] - nodes[j]) + nodes[i];
            temp2 = (nodes[j] - nodes[i]) + nodes[j];

            if (in_bounds(temp1, rowmax, colmax))
                antinodes.insert(temp1);
            if (in_bounds(temp2, rowmax, colmax))
                antinodes.insert(temp2);
        }
    }
}

void print_anti_nodes(const std::set<std::pair<int, int>> &antinodes)
{
    for (const auto &node : antinodes)
    {
        std::cout << "(" << node.first << ", " << node.second << ") ";
    }
    std::cout << std::endl; // Print a newline at the end
}

int main()
{
    auto start = chrono::high_resolution_clock::now();
    string filename = "./input.in";

    map<char, vector<pair<int, int>>> nodes;
    set<pair<int, int>> anti_nodes;
    char cell;

    ifstream inFile(filename);

    int row = 0;
    int col = 0;
    for (string line; getline(inFile, line); row++)
    {
        stringstream ss(line);
        for (col = 0; ss >> cell; col++)
        {
            if (cell != '.')
                nodes[cell].push_back({row, col});
        }
    }

    inFile.close();

    for (const auto &entry : nodes)
        get_anti_nodes(anti_nodes, entry.second, row, col);

    auto end = chrono::high_resolution_clock::now();
    auto duration = chrono::duration_cast<chrono::nanoseconds>(end - start);

    cout << "Time taken to execute: " << duration.count() / 1000 << " us" << endl;
    cout << "Answer: " << anti_nodes.size() << endl;

    return 0;
}
