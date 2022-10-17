

bool isPowerOfThree(int n){
    //method 1: climb up
    /*
    long long unsigned x = 1;
    if(n<=0){return 0;}
    if (n<1){n = 1/n;}
    while(1>0){
        if(n==x){return 1;}
        x*=3;
        if(x>n){return 0;}
    }
    */
    
    //method 2: climb down
    if(n<=0){return 0;}
    if(n==1){return 1;}
    if (n<1){n = 1/n;}
    while (1>0){
        if (n%3!=0){return 0;}
        n/=3;
        if (n==1){return 1;}
    }
}
