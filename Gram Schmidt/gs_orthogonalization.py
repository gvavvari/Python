using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Collections;

namespace gs_orthogonalization
{
    class Program
    {
        static void Main(string[] args)
        {
            double[,] array2D = new double[,] {{ 3, -6},{  4, -8},{ 0, 1}};
            int M = array2D.GetLength(0);
            int N = array2D.GetLength(1);
            double[,] U = new double[M, N];
            double[,] E = new double[M, N];
            double norm;
            double[] projection;

            for (int j = 0; j < N; j++)
            {
                projection = new double[j];
                for (int i = 0; i < M; i++)
                {
                    U[i, j] = array2D[i, j];
                    for (int p = 0; p < j; p++)
                        projection[p] += array2D[i, j] * E[i, p];
                }
                norm = 0;
                for (int i = 0; i < M; i++)
                {
                    for (int p = 0; p < j; p++)
                    {
                        U[i, j] -= projection[p] * E[i, p];
                    }
                    norm += Math.Pow(U[i, j], 2);
                }
                norm = Math.Sqrt(norm);
                for (int i = 0; i < M; i++)
                {
                    E[i, j] = U[i, j] / norm;
                }
            }
        }
    }
}
