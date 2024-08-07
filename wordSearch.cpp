#include <bits/stdc++.h>
using namespace std;

vector<vector<pair<int,int>>> wordCoords(vector<vector<char>> &grid, vector<string> &words) {
    vector<vector<pair<int,int>>> ans; 
    vector<pair<int,int>> dir = {{-1,0}, {1,0}, {0,1}, {0,-1}}; 
    vector<pair<int,int>> diagDir = {{-1,-1}, {-1,1}, {1,-1}, {1,1}};
    int m = grid.size(); 
    int n = grid[0].size(); 
    
    for(string str : words) {
        vector<pair<int,int>> coord; 
        bool wordPresent = false; 
        
        for(int i = 0; i < m && !wordPresent; i++) {
            for(int j = 0; j < n && !wordPresent; j++) {
                if(grid[i][j] == str[0]) {
                    // BFS for straight directions
                    queue<pair<int,int>> q; 
                    vector<pair<int,int>> tempCoord;
                    vector<vector<int>> vis(m, vector<int>(n, 0));
                    q.push({i, j});
                    vis[i][j] = 1;  
                    tempCoord.push_back({i, j});
                    int ind = 1;

                    while(!q.empty() && ind < str.size()) {
                        pair<int,int> frCrd = q.front();
                        int x = frCrd.first; 
                        int y = frCrd.second;  
                        q.pop(); 
                        for(pair<int,int> &d : dir) {
                            int nx = x + d.first; 
                            int ny = y + d.second; 
                            if(nx >= 0 && ny >= 0 && nx < m && ny < n && !vis[nx][ny] && grid[nx][ny] == str[ind]) {
                                q.push({nx, ny});
                                tempCoord.push_back({nx, ny});
                                vis[nx][ny] = 1;
                                ind++; 
                                break; 
                            }
                        }
                    }
                    if (ind == str.size()) {
                        coord = tempCoord;
                        wordPresent = true;
                    } else {
                        // Check diagonals
                        for(auto &d : diagDir) {
                            tempCoord.clear();
                            tempCoord.push_back({i, j});
                            int x = i, y = j;
                            ind = 1;
                            while(x + d.first >= 0 && x + d.first < m && y + d.second >= 0 && y + d.second < n && grid[x + d.first][y + d.second] == str[ind]) {
                                x += d.first;
                                y += d.second;
                                tempCoord.push_back({x, y});
                                ind++;
                                if(ind == str.size()) {
                                    coord = tempCoord;
                                    wordPresent = true;
                                    break;
                                }
                            }
                            if(wordPresent) break;
                        }
                    }

                    if(!wordPresent) {
                        coord.clear();
                        coord.push_back({-1, -1});
                    }
                }
            }
        }
        ans.push_back(coord); 
    }
    return ans;
}

int main() {
    vector<string> words = {
        "PEPPERONI", "HAM", "PINEAPPLE", "REDSAUCE","RED",
        "GARLIC", "SAUSAGE", "CHEESE", "CHICKEN" ,"PASTA" // pasta is not present so O/P will be -1
    };
    vector<vector<char>> grid = {
      // 0    1    2    3     4    5   6     7    8   9 
        {'H', 'C', 'R', 'H', 'A', 'G', 'P', 'A', 'U', 'P'}, //0
        {'D', 'E', 'E', 'R', 'I', 'S', 'C', 'N', 'L', 'P'}, //1
        {'S', 'A', 'D', 'P', 'N', 'A', 'H', 'N', 'I', 'A'}, //2
        {'C', 'L', 'S', 'M', 'O', 'U', 'R', 'N', 'G', 'C'}, //3
        {'H', 'D', 'A', 'E', 'R', 'S', 'E', 'I', 'A', 'I'}, //4
        {'I', 'H', 'U', 'H', 'E', 'A', 'H', 'C', 'R', 'E'}, //5
        {'C', 'E', 'C', 'P', 'P', 'G', 'H', 'O', 'L', 'L'}, //6
        {'K', 'P', 'E', 'P', 'P', 'E', 'G', 'I', 'I', 'S'}, //7
        {'E', 'N', 'L', 'N', 'E', 'I', 'S', 'D', 'C', 'C'}, //8
        {'N', 'E', 'S', 'S', 'P', 'I', 'R', 'I', 'I', 'E'}, //9
        {'N', 'R', 'E', 'M', 'H', 'S', 'C', 'S', 'A', 'I'}  // 10
    };
    
    vector<vector<pair<int,int>>> solution = wordCoords(grid, words); 
    for(int i = 0 ; i<solution.size() ; i++) {
        cout<<words[i];
        cout<<" ";
        for(pair<int,int> &crd: solution[i]) {
            if(crd.first == -1 && crd.second == -1)cout<<" is Not Found " ; 
            else{
            cout<<"->";
            cout<<" ";
            cout << "(" << crd.first << "," << crd.second << ") ";}
        }
        cout << endl;
    }
    
    return 0; 
}
