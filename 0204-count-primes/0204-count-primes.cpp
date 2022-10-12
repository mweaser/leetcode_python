class Solution {
public:
    int sieveOfEratosthenes(int n){
        
        if (n <= 2){
            return 0;
        }
        
        bool prime[n + 1];
        memset(prime, true, sizeof(prime));
        
        for (int p = 2; p * p <= n; p++){
            if (prime[p] == true){
                for (int i = p * p; i <= n; i += p){
                    prime[i] = false;
                }
            }
        }
        
        int count = 0;
        
        for (int p = 2; p < n; p++){
            if (prime[p]){
                count += 1;
            }
        }
        
        return count;
        
    }
    
    
    int countPrimes(int n) {
        return sieveOfEratosthenes(n);    
    }
};