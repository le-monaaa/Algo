import java.util.Scanner;

// 새의 수 N, 숫자 하나당 1초, 모든 새가 날아가기까지 총 몇 초가 걸리는지

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int count = 0;
        int i = 1;
        while(true){
            if(i<N){
                N -= i;
                count += 1;
                i += 1;
            }
            else if(i==N){
                count += 1;
                break;
            }
            else if(i>N){
                i = 1;
            }
        }
        System.out.println(count);

    }
}
