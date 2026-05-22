char* addBinary(char* a, char* b) {
    int carry=0,k=0,sum=0;
    // char o;
    int i=strlen(a)-1;
    int j=strlen(b)-1;
    int max=(strlen(a)>strlen(b))?(strlen(a)):strlen(b);
    char* o = (char*)malloc(max + 2);
    while (i>=0||j>=0||carry){
        sum=carry;
        if (i>=0){
            sum+=a[i]-'0';
            i--;
        }
        if (j>=0){
            sum+=b[j]-'0';
            j--;
        }

        if (sum==1){
            carry=0;
            o[k]='1';
        }
        else if (sum==2){
            carry=1;
            o[k]='0';
        }
        else if (sum==3){
             carry=1;
             o[k]='1';
        }
        else if( sum==0){
            carry=0;
            o[k]='0';
        }
        k++;
    }
    o[k]='\0';

    int left=0;
    int right=k-1;

    while(left<right){
        char temp= o[left];
        o[left]=o[right];
        o[right]=temp;

        left++;
        right--;
    }
    return o;

}

     