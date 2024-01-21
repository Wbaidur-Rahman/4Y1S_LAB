#include<bits/stdc++.h>
#include "mpi.h"
using namespace std;
int32_t main(int argc, char* argv[]){
    MPI_Init(&argc, &argv);

    int number_of_task;
    MPI_Comm_size(MPI_COMM_WORLD, &number_of_task);

    int task_id;
    MPI_Comm_rank(MPI_COMM_WORLD, &task_id);
    
    char *chunck;

    if(task_id == 0){
        string text = " ", pattern;
        cin >> pattern;
        string x;
        while(cin >> x){
            text += x + " ";
        }

        // now we need to devide the  text into number of task part
        int length = text.size() + 1;
        // [.............|.................|......................]
        int pattern_size = pattern.size();

        for(int i = 0; i < number_of_task; i++){
            int start_position = i * (length / number_of_task);
            start_position -= (pattern_size - 1);
            if(start_position < 0) start_position = 0;
            int end_position = (i + 1) * (length / number_of_task);
            if(i == number_of_task - 1){
                end_position = length;
            }
            //[start_position, end_position)
            int length_of_text_part = end_position - start_position;
            MPI_Send(&length_of_text_part, 1, MPI_INT, i, 0, MPI_COMM_WORLD);
            MPI_Send(text.c_str() + start_position, length_of_text_part, MPI_CHAR, i, 0, MPI_COMM_WORLD);

            MPI_Send(&pattern_size, 1, MPI_INT, i, 0, MPI_COMM_WORLD);
            MPI_Send(pattern.c_str() , pattern_size, MPI_CHAR, i, 0, MPI_COMM_WORLD);
            
        }
    }

        int length_of_text_part;
        MPI_Recv(&length_of_text_part, 1, MPI_INT, 0, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
        chunck = new char[length_of_text_part + 1];
        MPI_Recv(chunck, length_of_text_part, MPI_CHAR, 0, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);

        int pattern_size;
        MPI_Recv(&pattern_size, 1, MPI_INT, 0 , 0 , MPI_COMM_WORLD, MPI_STATUS_IGNORE);

        char *pat;
        pat = new char[pattern_size + 1];
        MPI_Recv(pat, pattern_size, MPI_CHAR, 0, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);

        

        int cnt = 0;

        for(int i = 0; i < length_of_text_part; i++){
            int match = 0;
            for(int j = 0; j < pattern_size; j++){
                if(chunck[i + j] == pat[j]){
                    match++;
                }
                else break;
            }
            if(match == pattern_size) cnt++;
        }
        MPI_Send(&cnt, 1, MPI_INT, 0, 0, MPI_COMM_WORLD);

        if(task_id == 0){
            int ans = 0;
            int cur = 0;
            for(int i = 0; i < number_of_task; i++){
                MPI_Recv(&cur, 1, MPI_INT, i, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
                ans += cur;
            }
            cout << "Total occurence found : " << ans << endl;
        }

    MPI_Finalize();
}