#include <bits/stdc++.h>
using namespace std ; 

vector<vector<pair<int,int>>> wordCoords(vector<vector<char>> &grid , vector<string> & words ){
        vector<vector<pair<int,int>>> ans ; 
        vector<pair<int,int>> dir ={{-1,0}, {1,0}, {0,1}, {0,-1}}; 
        int m = grid.size() ; 
        int n = grid[0].size() ; 
        for(string str : words ){
            vector<pair<int,int>> coord ; 
            vector<vector<int>> vis (m , vector<int>(n,0));
            bool wordPresent = false ; 
            for(int i = 0 ; i<m && !wordPresent; i++){
                for(int j = 0 ; j<n &&!wordPresent ; j++){
                    int ind = 0 ; 
                    if(grid[i][j] == str[ind] ){
                        queue<pair<int,int>> q ; 
                        vector<pair<int, int>> tempCoord;
                        tempCoord.push_back({i,j});
                        q.push({i,j}) ;
                        vis[i][j] = 1 ;  
                        ind ++ ; 
                        while(!q.empty()){
                            pair<int,int> frCrd = q.front() ;
                            int x = frCrd.first ; 
                            int y = frCrd.second ;  
                            q.pop() ; 
                            for(pair<int,int> &d  : dir){
                                int dx = d.first ; 
                                int dy = d.second ; 
                                int nx = x +dx ; 
                                int ny = y+ dy ; 
                                if(nx>=0 && ny>=0 && nx<m && ny<n && !vis[nx][ny] && grid[nx][ny] == str[ind]){
                                    q.push({nx,ny});
                                    tempCoord.push_back({nx, ny});
                                    vis[nx][ny] = 1 ;
                                    ind++ ; 
                                    break ; 
                                }
                            }
                        }
                        if (ind == str.size()) {
                            coord = tempCoord;
                            wordPresent = true;
                    } else {
                        coord.clear();
                        coord.push_back({-1, -1});
                    }
                    }
                }
            }ans.push_back(coord) ; 
        }
        return ans ;
    };
int main(){
    vector<string> words = {"RED" , 
        "GARLIC", "SAUSAGE", "CHICKEN","CHEESE",
    };
    vector<vector<char>> grid = {
        {'H', 'C', 'R', 'H', 'A', 'G', 'P', 'A', 'U', 'P'},
        {'D', 'E', 'E', 'R', 'I', 'S', 'C', 'N', 'L', 'P'},
        {'S', 'A', 'D', 'P', 'N', 'A', 'H', 'N', 'I', 'A'},
        {'C', 'L', 'S', 'M', 'O', 'U', 'R', 'N', 'G', 'C'},
        {'H', 'D', 'A', 'E', 'R', 'S', 'E', 'I', 'A', 'I'},
        {'I', 'H', 'U', 'H', 'E', 'A', 'H', 'C', 'R', 'E'},
        {'C', 'E', 'C', 'P', 'P', 'G', 'H', 'O', 'L', 'L'},
        {'K', 'P', 'E', 'P', 'P', 'E', 'G', 'I', 'I', 'S'},
        {'E', 'N', 'L', 'N', 'E', 'I', 'S', 'D', 'C', 'C'},
        {'N', 'E', 'S', 'S', 'P', 'I', 'R', 'I', 'I', 'E'},
        {'N', 'R', 'E', 'M', 'H', 'S', 'C', 'S', 'A', 'I'}};
     vector<vector<pair<int,int>>> solution = wordCoords(grid,words) ; 
    for(auto &vec1 : solution){
            for(pair<int,int> & crd: vec1){
                cout<<crd.first;
                cout<<crd.second;
                cout<<" ";
    }
    cout<<endl ;
    }
        return 0 ; }