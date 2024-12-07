#include <iostream>
using namespace std;

// Helper function to calculate the number of digits in an integer
int numDigits(int n)
{
    int digits = 0;
    while (n > 0)
    {
        n /= 10;
        ++digits;
    }
    return digits;
}

// Function to check if a ends with b
bool endsWith(int a, int b)
{
    int bDigits = numDigits(b);
    int divisor = 1;
    for (int i = 0; i < bDigits; ++i)
    {
        divisor *= 10;
    }
    return (a % divisor) == b;
}

// Function to trim b from the end of a
int trim(int a, int b)
{
    int bDigits = numDigits(b);
    int divisor = 1;
    for (int i = 0; i < bDigits; ++i)
    {
        divisor *= 10;
    }
    return a / divisor;
}

int main()
{
    int a = 12345;
    int b = 45;

    if (endsWith(a, b))
    {
        cout << a << " ends with " << b << endl;
        cout << "Trimmed value: " << trim(a, b) << endl;
    }
    else
    {
        cout << a << " does not end with " << b << endl;
    }

    return 0;
}