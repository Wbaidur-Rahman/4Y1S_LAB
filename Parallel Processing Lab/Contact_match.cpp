#include<bits/stdc++.h>
#include<mpi.h>

using namespace std;

void send_a_number(int num,int to){
    MPI_Send(&num, 1, MPI_INT, to, 0, MPI_COMM_WORLD);
}
void send_a_string(string str,int to){
    int len = str.length();
    MPI_Send(&str[0], len, MPI_CHAR, to, 0, MPI_COMM_WORLD);
}

int receive_a_number(int form){
    int num;
    MPI_Recv(&num,1,MPI_INT, form, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
    return num;
}

string recv_a_string(int form){
    int len = receive_a_number(form);
    char* str = new char[len];
    MPI_Recv(str, len, MPI_CHAR, form, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
    return string(str);
}

vector<string> get_vect(string str){
    stringstream ss(str);
    vector<string> v;
    string s;
    while(ss >> s){
        v.push_back(s);
    }
    return v;
}

void check(string name, string pat, string phn){
    int m = 0;
    for(int i=0;name[i];i++){
        if(m<pat.length() && name[i]==pat[m]) m++;
    }

    if(m==pat.length())
        cout << name << " " << phn << endl;
}

int main(int argc, char* argv[]){
    MPI_Init(&argc, &argv);

    int number_of_task;
    MPI_Comm_size(MPI_COMM_WORLD, &number_of_task);

    int rank;
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);

    if(rank == 0){
        // cout << "Enter number of contacts : \n";
        int n;
        cin >> n;

        vector<string> contacts(n),phn_num(n);
        for(int i=0;i<n;i++){
            cin >> contacts[i] >> phn_num[i];
        }

        clock_t  start_time, end_time;
        start_time = clock();

        string name;
        cin >> name;

        cout << name << endl;

        for(int i=1; i<number_of_task; i++){
            int start = i*(n/number_of_task);
            int end = (i+1)*(n/number_of_task);
            if(i==number_of_task-1) end = n;

            string str1="",str2="";
            for(int j=start; j<end; j++){
                str1 += contacts[j]+"\n";
                str2 += phn_num[j]+"\n";
            }
        
            int str1_length = str1.length();
            int str2_length = str2.length();
            int name_length = name.length();

            send_a_number(str1_length, i);
            send_a_string(str1, i);
            send_a_number(str2_length, i);
            send_a_string(str2, i);
            send_a_number(name_length, i);
            send_a_string(name, i);

        }

        string str1="",str2="";
        for(int j=0;j<(n/number_of_task);j++){
            str1 += contacts[j]+"\n";
            str2 += phn_num[j]+"\n";
        }

        vector<string> nam = get_vect(str1);
        vector<string> phn_n = get_vect(str2);

        // cout << nam.size() << endl;

        for(int i=0;i<nam.size();i++){
            check(nam[i], name, phn_n[i]);
        }
        for(int i=1;i<number_of_task;i++){
        receive_a_number(i);
        }
        end_time = clock();

        double total_time = double(end_time-start_time)/double(CLOCKS_PER_SEC);
    }
    else{
        string names = recv_a_string(0);
        vector<string> name_list = get_vect(names);
        string phn_numers = recv_a_string(0);
        vector<string> phn_list = get_vect(phn_numers);
        // string name = recv_a_string(0);
        string pattern = recv_a_string(0);

        // cout << name << endl;
        for(int i=0;i<name_list.size();i++){
            check(name_list[i], "Smith", phn_list[i]);
        }
        send_a_number(1, 0);
    }

    MPI_Finalize();
}