import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;
 
public class Main {
    static int N, M;                    // 캠퍼스의 세로, 가로 크기
    static int[] dx = {-1, 0, 1, 0};    // 상, 하 이동
    static int[] dy = {0, -1, 0, 1};    // 좌, 우 이동
    static char[][] campus;                // 2차원 캠퍼스 배열
    static boolean[][] visited;            // 2차원 방문 체크 배열                
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());    
        M = Integer.parseInt(st.nextToken());    
        campus = new char[N][M];                    
        visited = new boolean[N][M];                
        int x = -1, y = -1;        // 도연이의 현재 위치
        
        for (int i = 0; i < N; i++) {
            String line = br.readLine();
            for (int j = 0; j < M; j++) {
                campus[i][j] = line.charAt(j);
                if (campus[i][j] == 'I') {    // 해당 좌표에 있는 글자가 도연이에 해당한다면
                    x = i;    // 도연이의 x좌표 위치 저장
                    y = j;    // 도연이의 y좌표 위치 저장
                }
            }
        }
        
        int count = bfs(x, y);        // 도연이가 만날 수 있는 사람의 수
        
        if (count != 0) {    // 도연이가 사람을 만날 수 있는 경우
            System.out.println(count);    // 도연이가 만날 수 있는 사람의 수 출력
        } else {    // 도연이가 아무도 만나지 못한 경우
            System.out.println("TT");    
        }
    }
    
    public static int bfs(int x, int y) {
        Queue<int[]> queue = new LinkedList<>();    // bfs 수행을 위한 큐
        queue.add(new int[] {x, y});    // 큐에 도연이의 위치를 삽입
        visited[x][y] = true;            // 도연이의 위치를 방문 체크
        int count = 0;                    // 도연이가 만날 수 있는 사람의 수
        
        while (!queue.isEmpty()) {
            int[] now = queue.poll();    // 큐에서 현재 좌표 뽑기
            
            // 현재 위치 기준으로 상하좌우 탐색
            for (int i = 0; i < 4; i++) {
                int nx = now[0] + dx[i];    // 인접한 x좌표
                int ny = now[1] + dy[i];    // 인접한 y좌표
                
                // 인접한 좌표 인덱스가 유효 범위에 속하지 않는다면 건너뛰기
                if (nx < 0 || ny < 0 || nx >= N || ny >= M) {
                    continue;
                }
                
                // 인접 좌표를 이미 방문했거나, 벽이라면 건너뛰기
                if (visited[nx][ny] || campus[nx][ny] == 'X') {
                    continue;
                }
                
                queue.add(new int[] {nx, ny});    // 큐에 인접 좌표를 삽입
                visited[nx][ny] = true;            // 인접 좌표를 방문 체크
                
                if (campus[nx][ny] == 'P') {    // 인접 위치에 사람이 있다면
                    count++;    // 도연이가 만날 수 있는 사람의 수 1 증가
                }
            }
        }
        
        return count;    // 도연이가 만날 수 있는 사람의 수 리턴
    }
}