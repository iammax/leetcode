

bool isPerfectSquare(int num){ 
    long long unsigned sq;
    for (long long unsigned i  = 1; i <= num; i++){
        sq = i*i;
        if(sq==num){return 1;}
        if(sq > num){return 0;}
    }
    return 0;
}
