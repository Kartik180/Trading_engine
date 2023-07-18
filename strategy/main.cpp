    #include <bits/stdc++.h>
    using namespace std;
    int func(long long  n)
    {
        int sum = 0;
        if (n < 10)
        {
            return n;
        }
        while (n > 0)
        {
            sum += n % 10;
            n = n / 10;
        }
        return 1ll*func(sum);
    }
    int main()
    {
        string n;
        int  k;
        cin >> n >> k;
        long long sum = 0;
        for(int i=0; i<n.length(); i++)
        {
            sum += (n[i] - '0');
        }
        sum *= k;
        cout << func(sum);
        return 0;
    }