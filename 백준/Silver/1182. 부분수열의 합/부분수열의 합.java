import java.io.*;
import java.util.*;

public class Main {
	
	static int N,S,cnt=0;
	static int[] num;
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();	//정수 개수 
		S = sc.nextInt();	//목표 합이 되는 수
		num= new int[N];	//정수 담는 배열 

		for(int i=0;i<N;i++)
			num[i]=sc.nextInt();
		
		dfs(0,0);
		
		if(S==0)	//부분수열 크기 0
			cnt-=1;
		System.out.println(cnt);
		
	}// main()
	
	static void dfs(int depth, int sum) {
		if(depth==N) {
			if(sum==S)	cnt++;
			return;
		}
		
		dfs(depth+1,sum+num[depth]);	//지금 위치원소를 선택 했거나
		dfs(depth+1,sum);				//안했거나
	}
		
}