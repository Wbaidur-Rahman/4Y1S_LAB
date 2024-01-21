#include<bits/stdc++.h>
#include "mpi.h"
using namespace std;
void send_a_number(int number, int to){
    MPI_Send(&number, 1, MPI_INT, to, 0, MPI_COMM_WORLD);
}

void send_a_string(string str, int to){
    int length = str.size() + 1;
    send_a_number(length, to);
    MPI_Send(&str[0], length, MPI_CHAR, to, 0, MPI_COMM_WORLD);
}

int receive_a_number(int from){
    int length;
    MPI_Recv(&length, 1, MPI_INT, from, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
    return length;
}

string receive_a_string(int from){
    int length  = receive_a_number(from);
    char *buffer = new char[length];
    MPI_Recv(buffer, length, MPI_CHAR, from, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
    return string(buffer);
}

string generate_string(vector<string> &str, int start_position, int end_position){
    string ans = "";

    for(int i = start_position; i < end_position; i++){
        ans += str[i] + "\n";
    }
    return ans;
}
vector<string> get_string_list(string str){
    stringstream ss(str);
    vector<string> ans;
    string word;
    while(ss >> word){
        ans.push_back(word);
    }
    return ans;
}

void check(string text, string pattern, string phone){
    int n = text.size();
    int m = pattern.size();
    int  cnt = 0;
    for(int i = 0; i < n; i++){
        if(text[i] == pattern[cnt]){
            cnt++;
            if(cnt == m){
                // matched
                cout << text << " " << phone << endl;
                return;
            }
        }
        else cnt=0;
    }
}


int32_t main(int argc, char* argv[]){
    MPI_Init(&argc, &argv);

    ifstream myfile;
    
        int number_of_task;
        MPI_Comm_size(MPI_COMM_WORLD, &number_of_task);

        int task_id;
        MPI_Comm_rank(MPI_COMM_WORLD, &task_id);

        double time = 0;
        if(task_id == 0){
        for(int i=1;i<argc;i++){
            myfile.open(argv[i]);

            int n;
            myfile >> n;
            cout << n << endl;
            vector<string> name_list(n), phone_list(n);
    
            string pattern;
            myfile >> pattern;
            
            for(int i = 0; i < n; i++){
                myfile >> name_list[i] >> phone_list[i];
            }

            // time calculation start
            clock_t start, end;
            start = clock();
            // data send korbo.

            for(int i =  1; i < number_of_task; i++){
                int start_position = i *  (n / number_of_task);
                int end_position = (i + 1) * (n / number_of_task);

                string for_send_name = generate_string(name_list, start_position, end_position);
                send_a_string(for_send_name, i);
                string for_send_phone = generate_string(phone_list, start_position, end_position);
                send_a_string(for_send_phone, i);
                send_a_string(pattern, i);
            }
            // send done
            for(int i = 0;i <  n / number_of_task; i++){
                check(name_list[i], pattern, phone_list[i]);
            }
            // time calculation end
            end = clock();
            double time_taken = double(end - start) / double(CLOCKS_PER_SEC);
            time += time_taken;
            myfile.close();
        }
        }
        else{
        for(int i=1;i<argc;i++){
            string name = receive_a_string(0);
            vector<string> name_list = get_string_list(name);
            string phone = receive_a_string(0);
            vector<string> phone_list = get_string_list(phone);
            string pattern = receive_a_string(0);
            // main work;

            int n = phone_list.size();
            for(int i = 0; i < n; i++){
                check(name_list[i], pattern, phone_list[i]);
            }
        };
    }

    cout << time << endl;
    MPI_Finalize();
}