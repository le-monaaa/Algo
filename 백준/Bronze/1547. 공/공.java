import java.util.Scanner;

// 컵의 위치를 바꾼 횟수 M(M<=50)
// M lines X, Y (X, Y <=3)
// 공이 사라져서 컵 밑에 없는 경우는 -1

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int M = sc.nextInt(); // 컵의 위치를 바꾸는 횟수
        int[] cups = new int[4];
        cups[0] = 0;
        cups[1] = 1;
        cups[2] = 0;
        cups[3] = 0;

        for(int i=0; i<M; i++){
            int x = sc.nextInt();
            int y = sc.nextInt();
            if(x!=y){
                int temp = cups[x];
                cups[x] = cups[y];
                cups[y] = temp;
            }
        }
        for(int i=1; i<4; i++){
            if (cups[i] == 1){
                System.out.println(i);
                break;
            }
        
        }
    }
}
