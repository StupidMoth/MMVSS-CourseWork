#include <iostream>
#include <vector>
#include <fstream>
#include <algorithm>

using namespace std;
double inf = 1000000;
double w[20][20];
int k = 0;
void Dijkstra(int st)
{
    int n = 20;
    bool visited[n];
    double D[n];
    int p[n];
    for(int i=0;i<n;i++)
    {
        p[i] = st;
        D[i]=w[st][i];
        visited[i]=false;
    }
    D[st]=0;
    int index=0,u=0;
    for (int i=0;i<n;i++)
    {
        int min=inf;
        for (int j=0;j<n;j++)
        {
            if (!visited[j] && D[j]<min)
            {
                min=D[j];
                index=j;
            }
        }
        u=index;
        visited[u]=true;
        for(int j=0;j<n;j++)
        {
            if (!visited[j] && w[u][j]!=inf && D[u]!=inf && (D[u]+w[u][j]<D[j]))
            {
                D[j]=D[u]+w[u][j];
                p[j] = u;

            }
        }
    }

    for (int i = 0; i < 20; i++) {
        cout << p[i]  + 1 << " ";
        k += p[i] + 1;
    }
    cout << endl;

}
int main() {
    ifstream fin("mas.txt");
    int n = 20;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            fin >> w[i][j];
            if(w[i][j] == 0)
                w[i][j] = inf;
        }
    }
    for (int i = 0; i < n; i++)
        Dijkstra(i);
    cout << k;

    return 0;
}
