#include <bits/stdc++.h>
using namespace std;
 
bool isPrime(long long int n)
{
    // Corner case
    if (n <= 1)
        return false;
 
    // Check from 2 to n-1
    for (long long int i = 2; i <= n / 2; i++)
        if (n % i == 0)
            return false;
 
    return true;
}
int main() {
    long long int z = 10000;
    long long int prime[1000];
    long long int n = 0;
    long long int i = 0, sum = 0, c = 0, m = 0;
    while(i < 1000) {
        if(isPrime(n)) {
            prime[i] = n;
            i++;
        }
        n++;
    }
    for(auto p: prime)
        cout << p << endl;
}

