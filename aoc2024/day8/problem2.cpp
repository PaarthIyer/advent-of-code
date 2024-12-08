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
bool in_bounds(pair<int, int> p, int rowmax, int colmax)
{
    return (p.first >= 0 && p.first < rowmax && p.second >= 0 && p.second < colmax);
}
///////////////////////////////////////////////////////////////////////////

void get_anti_nodes(set<pair<int, int>> &antinodes,
                    const vector<pair<int, int>> &nodes,
                    int rowmax, int colmax)
{
    pair<int, int> temp, delta;
    int mult;
    bool valid, valid2;
    for (int i = 0; i < nodes.size(); i++)
    {
        for (int j = i + 1; j < nodes.size(); j++)
        {
            mult = 0;
            delta = {nodes[i].first - nodes[j].first, nodes[i].second - nodes[j].second};
            while (true)
            {
                temp = {(nodes[i].first + delta.first) * mult, (nodes[i].second + delta.second) * mult};
                valid = in_bounds(temp, rowmax, colmax);

                if (valid)
                    antinodes.insert(temp);

                temp = {(nodes[j].first - delta.first) * mult, (nodes[j].second - delta.second) * mult};
                valid2 = in_bounds(temp, rowmax, colmax);

                if (valid2)
                    antinodes.insert(temp);

                if (!(valid || valid2))
                    break;
                mult++;
            }
        }
    }
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
