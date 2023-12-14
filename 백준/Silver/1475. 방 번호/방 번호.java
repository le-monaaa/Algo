import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] count = new int[] {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
        String N = sc.nextLine();
        char[] numArr = N.toCharArray();

        for(int i=0; i<numArr.length; i++){

                count[(int)(numArr[i]-'0')] += 1;
            }
        int maxCount = 0;
        for(int i=0; i<count.length; i++){
            if(!(i==6 || i==9)){
                if(count[i]>maxCount){
                    maxCount = count[i];
                }
            }
        }
        int ns = count[6] + count[9];
        if(ns%2 != 0) {
            ns = ns/2 + 1;
        }
        else{
            ns /=2;
        }
        System.out.println(maxCount >= ns ? maxCount : ns);
    }
}
