    int g_c_d(int a,int b){
        if(b == 0){
            return a;
        }
        else{
            return g_c_d(b,a%b);
        }
    }
