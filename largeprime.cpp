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

int main () {
    
    long long int a = 0, sum = 0, c = 0;
    while(sum < 1000000) {
        a++;
        if(isPrime(a)) {
            sum += a;
        }
    }
    cout << sum << endl;
}