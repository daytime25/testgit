/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package congtaozailai;

import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.io.LineNumberReader;

/**
 *
 * @author ming
 */
public class LinkedList {

    // 读取文件指定行。
    static void readAppointedLineNumber(File sourceFile, int lineNumber)
            throws IOException {
        FileReader in = new FileReader(sourceFile);
        LineNumberReader reader = new LineNumberReader(in);
        String line = null;
        if (lineNumber <= 0 || lineNumber > getTotalLines(sourceFile)) {
            System.out.println("不在文件的行数范围(1至总行数)之内。");
            System.exit(0);
        }
        //int lines = 0;
        while ((line=reader.readLine()) != null) {
            
                System.out.println(reader.getLineNumber()+""+line);
                System.exit(0);
            
        }
        reader.close();
        in.close();
    }
// 文件内容的总行数。

    static int getTotalLines(File file) throws IOException {
        FileReader in = new FileReader(file);
        LineNumberReader reader = new LineNumberReader(in);
        String s = reader.readLine();
        int lines = 0;
        while (s != null) {
            lines++;
            s = reader.readLine();
        }
        reader.close();
        in.close();
        return lines;
    }

    public int maxSunSunl(int[] a) {
        int maxSum = 0;
        //a[]=[1,4,5];
        for (int i = 0; i <= a.length; i++) {
            for (int j = i; i < a.length; j++) {
                int thisSum = 0;
                for (int k = i; k <= j; k++) {
                    thisSum += a[k];
                }
                if (thisSum > maxSum) {
                    maxSum = thisSum;
                }
            }
            //System.out.println(maxSum);
        }
        return maxSum;

    }

    public double prorelprim(int n) {
        int rel = 0, tot = 0;
        for (int i = 1; i <= n; i++) {
            for (int j = i + 1; i < n; j++) {
                tot++;
                if (gcd(i, j) == 1) {
                    rel++;
                }
            }
            //System.out.println(maxSum);
        }
        return (double) rel / tot;

    }

    private int gcd(int num1, int num2) {
        while (num1 != num2) {
            if (num1 > num2) {
                num1 = num1 - num2;
            } else {
                num2 = num1 - num2;
            }
        }
        return num1;

    }

    public static void main(String[] args) throws IOException {
        //Congtaozailai test = new Congtaozailai();
        // test.maxSunSunl();
       /* int size = 5;
         size *= 2;
         size *= size;
         size /= 100;
         System.out.println(size);

         final int max_rows = 10;
         for (int row = 1; row <= max_rows; row++) {
         for (int star = 1; star <= row; star++) {

         }
         System.out.println();
         }*/

        // 指定读取的行号
        int lineNumber = 2;
// 读取文件
        File sourceFile = new File("/javaPro/congtaozailai/input.txt");
// 读取指定的行
        readAppointedLineNumber(sourceFile, lineNumber);
// 获取文件的内容的总行数
      //  System.out.println(getTotalLines(sourceFile));
    }
}
