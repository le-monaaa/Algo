import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int L = sc.nextInt();
        int[] f = new int[N];
        for(int i=0; i<N; i++){
            f[i] = sc.nextInt();
        }
        Arrays.sort(f);
        for(int i=0; i<N; i++){
            if(L>=f[i]){
                L+=1;
            }
        }
        System.out.println(L);
    }
}
