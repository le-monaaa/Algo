import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int T = sc.nextInt();
        for(int i=0; i<T; i++){
            int d = sc.nextInt();
            for(int t=0; t<d; t++){
                if(d==1){
                    System.out.println(0);
                    break;
                }
                double dt = Math.pow(t, 2);
                    if(d==dt+t){
                        System.out.println(t);
                        break;
                    }
                    else if(d<dt+t){
                        System.out.println(t-1);
                        break;
                    }
                }
        }
    }
}
