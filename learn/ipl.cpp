    #include<bits/stdc++.h>
    using namespace std;
    long long int arr[10]={0};
    void prob(int Gt,int CSk,int Mi,int LSg,int Rr,int KKr,int RCb,int PBKs,int SRh,int Dc){
        arr[0]+=0ll+Gt;
        arr[1]+=0ll+CSk;
        arr[2]+=0ll+Mi;
        arr[3]+=0ll+LSg;
        arr[4]+=0ll+Rr;
        arr[5]+=0ll+KKr;
        arr[6]+=0ll+RCb;
        arr[7]+=0ll+PBKs;
        arr[8]+=0ll+SRh;
        arr[9]+=0ll+Dc;
    }
    void compute(vector<pair<string,string>>&fixtures,int Gt,int CSk,int Mi,int LSg,int Rr,int KKr,int RCb,int PBKs,int SRh,int Dc,int len,int k){
        if(len==k){
            prob(Gt,CSk, Mi, LSg, Rr, KKr, RCb, PBKs, SRh, Dc);
        }
        else{
            string a = fixtures[len].first;
            string b=fixtures[len].second;
            if(a=="GT" || b=="GT"){
                compute(fixtures,Gt+2,CSk, Mi, LSg, Rr, KKr, RCb, PBKs, SRh, Dc,len+1,k);
            }
            if(a=="CSK" || b=="CSK"){
                compute(fixtures,Gt,CSk+2, Mi, LSg, Rr, KKr, RCb, PBKs, SRh, Dc,len+1,k);
            }
            if(a=="MI" || b=="MI"){
                compute(fixtures,Gt,CSk, Mi+2, LSg, Rr, KKr, RCb, PBKs, SRh, Dc,len+1,k);
            }
            if(a=="LSG" || b=="LSG"){
                compute(fixtures,Gt,CSk, Mi, LSg+2, Rr, KKr, RCb, PBKs, SRh, Dc,len+1,k);
            }
            if(a=="RR" || b=="RR"){
                compute(fixtures,Gt,CSk, Mi, LSg, Rr+2, KKr, RCb, PBKs, SRh, Dc,len+1,k);
            }
            if(a=="KKR" || b=="KKR"){
                compute(fixtures,Gt,CSk, Mi, LSg, Rr, KKr+2, RCb, PBKs, SRh, Dc,len+1,k);
            }
            if(a=="PBKS" || b=="PBKS"){
                compute(fixtures,Gt,CSk, Mi, LSg, Rr, KKr, RCb, PBKs+2, SRh, Dc,len+1,k);
            }
            if(a=="RCB" || b=="RCB"){
                compute(fixtures,Gt,CSk, Mi, LSg, Rr, KKr, RCb+2, PBKs, SRh, Dc,len+1,k);
            }
            if(a=="DC" || b=="DC"){
                compute(fixtures,Gt,CSk, Mi, LSg, Rr, KKr, RCb, PBKs, SRh, Dc+2,len+1,k);
            }
            if(a=="SRH" || b=="SRH"){
                compute(fixtures,Gt,CSk, Mi, LSg, Rr, KKr, RCb, PBKs, SRh+2, Dc,len+1,k);
            }
        }
    }
    int main()
    {
        vector <pair<string ,string>> fixtures = {
            {"CSK", "DC"},
            {"KKR", "RR"},
            {"MI", "GT"},
            {"SRH", "LSG"},
            {"DC", "PBKS"},
            {"RR", "RCB"},
            {"CSK", "KKR"},
            {"GT", "SRH"},
            {"LSG", "MI"},
            {"PBKS", "DC"},
            {"SRH", "RCB"},
            {"PBKS", "RR"},
            {"DC", "CSK"},
            {"KKR", "LSG"},
            {"MI","SRH"},
            {"RCB","GT"}
        }; 
        int k=fixtures.size();
        int d=pow(2,k);
        compute(fixtures,16,13,12,11,10,10,10,10,8,8,0,k);
        cout<<"GT"<<arr[0]/d<<endl;
        cout<<"CSK"<<arr[1]/d<<endl;
        cout<<"MI"<<arr[2]/d<<endl;
        cout<<"LSG"<<arr[3]/d<<endl;
        cout<<"RR"<<arr[4]/d<<endl;
        cout<<"KKR"<<arr[5]/d<<endl;
        cout<<"RCB"<<arr[6]/d<<endl;
        cout<<"PBKS"<<arr[7]/d<<endl;
        cout<<"SRH"<<arr[8]/d<<endl;
        cout<<"DC"<<arr[9]/d<<endl;
        return 0;
    }
