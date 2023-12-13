import java.util.Arrays;
import java.util.Scanner;



public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int T = sc.nextInt();
        for(int i=0; i<T; i++){
            int[] arr = new int[5];
            for(int k=0; k<5; k++){
                arr[k] = sc.nextInt();
            }
            Arrays.sort(arr);
            if(arr[3]-arr[1]>=4){
                System.out.println("KIN");
            }
            else {
                int sum = Arrays.stream(Arrays.copyOfRange(arr, 1, 4)).sum();
                System.out.println(sum);
            }
        }

    }
}
