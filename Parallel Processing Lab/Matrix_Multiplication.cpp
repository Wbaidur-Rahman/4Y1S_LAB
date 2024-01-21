#include <bits/stdc++.h>
#include <mpi.h>

using namespace std;

vector<int> multiplication(int *a, int *b, int num_of_matrix, int M, int N, int P){
   vector<int> output_matrix(num_of_matrix*M*P);

   for(int cnt=0;cnt<num_of_matrix; cnt++){
      int add_a = cnt*M*N;
      int add_b = cnt*N*P;
      int add_c = cnt*M*P;

      for(int i=0; i<M; i++){
         for(int j=0; j<P; j++){
            int sum = 0;
            for(int k=0;k<N;k++){
               sum += a[add_a + i*N + k]*b[add_b + j*N + k];
            }
            output_matrix[add_c + i*P + j]= sum;
         }
      }
   }

   return output_matrix;
}

int main(int argc, char* argv[]) {
   MPI_Init(&argc, &argv);

   int number_of_processes;
   MPI_Comm_size(MPI_COMM_WORLD, &number_of_processes);

   int rank;
   MPI_Comm_rank(MPI_COMM_WORLD, &rank);

   int start,num,M,N,P,size;
   clock_t start_time, end_time; 

   if (rank == 0) {
      cin >> num >> M >> N >> P;

      int* a = new int[num*M*N];
      int* b = new int[num*N*P];

      
      printf("values = %d %d %d %d\n",num,M,N,P);
      size = (num/number_of_processes);


      for(int i=0;i<num*M*N;i++) a[i]=1;
      for(int i=0;i<num*P*N;i++) b[i]=1;
      
      start_time = clock();

      for (int i = 1; i < number_of_processes; i++) {
         start = i*size;
         
         MPI_Send(&size, 1, MPI_INT, i, 0, MPI_COMM_WORLD);
         MPI_Send(&M, 1, MPI_INT, i, 0, MPI_COMM_WORLD);
         MPI_Send(&N, 1, MPI_INT, i, 0, MPI_COMM_WORLD);
         MPI_Send(&P, 1, MPI_INT, i, 0, MPI_COMM_WORLD);
         
         
         MPI_Send(&(a[start*M*N]), size*M*N, MPI_INT, i, 0, MPI_COMM_WORLD);
         MPI_Send(&(b[start*N*P]), size*N*P, MPI_INT, i, 0, MPI_COMM_WORLD);
      }

         vector<int> c0 = multiplication(&a[0], &b[0], size, M, N, P);
      
         vector<int> c(M*P);  
         for (int i = 1; i < number_of_processes; i++) {
            MPI_Recv(&c[0], M*P, MPI_INT, i, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
            // for(int i=0; i<M*P;i++){
            //       cout << c[i] << " ";
            //       if((i+1)%P==0) cout << " == Hello " << endl;
            //    }
            //    cout << endl;
         }

         end_time = clock();
         cout << "Total time needed = " << double(end_time- start_time)/double(CLOCKS_PER_SEC) << endl;

         delete[] a;
         delete[] b;
   }
   
   else{
      MPI_Recv(&size, 1, MPI_INT, 0, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
      MPI_Recv(&M, 1, MPI_INT, 0, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
      MPI_Recv(&N, 1, MPI_INT, 0, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
      MPI_Recv(&P, 1, MPI_INT, 0, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);

      vector<int> a(size*M*N);
      vector<int> b(size*P*N);
      vector<int> c(size*P*M);
      
      
      MPI_Recv(&a[0], (size*M*N), MPI_INT, 0, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
      MPI_Recv(&b[0], (size*P*N), MPI_INT, 0, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);

      c = multiplication(&a[0], &b[0], size, M, N, P);
      MPI_Send(&c[0], M*P, MPI_INT, 0, 0, MPI_COMM_WORLD);
   }

   MPI_Finalize();
}
