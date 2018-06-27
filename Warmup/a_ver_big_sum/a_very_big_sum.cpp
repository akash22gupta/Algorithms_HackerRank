#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
   long long int n;
    cin>>n;
    long long int sum=0;
    vector <long long int> a(n);
    for(int i=0;i<n;i++){
        cin>>a[i];
        sum+=a[i];
    }
    cout<<sum;
    return 0;
}
