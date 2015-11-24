/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package congtaozailai;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.io.LineNumberReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;
import java.util.PriorityQueue;

/**
 *
 * @author ming
 */
public class bujkesiyi {

    public static double[] writeToDat(String path) {
        File file = new File(path);
        List list = new ArrayList();
        double[] nums = null;
        try {
            //BufferedReader bw = new BufferedReader(new FileReader(file));
            String line = null;
            LineNumberReader l = new LineNumberReader(new FileReader(file));
            l.setLineNumber(10); //跳到第10行
            for (int i = 10; i <= 20; i++) {
                System.out.println(l.readLine()); //显示第10-100行
            }
           
            //因为不知道有几行数据，所以先存入list集合中
            while ((line = l.readLine()) != null) {
                list.add(line);
            } 
            l.close();
            //bw.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
        //确定数组长度
        nums = new double[list.size()];
        for (int i = 0; i < list.size(); i++) {
            String s = (String) list.get(i);
            nums[i] = Double.parseDouble(s);
        }
        return nums;
    }

    public static void main(String[] args) {
        long startTime = System.nanoTime();

        String path = "/javaPro/congtaozailai/input.txt";
        double[] nums = writeToDat(path);
        Comparator<Double> cmp;
        cmp = new Comparator<Double>() {
            public int compare(Double e1, Double e2) {
                return (int) (e2 - e1);
            }
        };
        PriorityQueue<Double> pq = new PriorityQueue<Double>(20, cmp);
        for (int i = 0; i < nums.length; i++) {
            System.out.println(nums[i]);
            pq.add(nums[i]);
        }
        /* public static void main(String[] args) throws FileNotFoundException{
         Scanner scanner=new Scanner(new FileInputStream("/javaPro/congtaozailai/input.txt"));
         // Queue<Float> FloatPriorityQueue = new PriorityQueue<>();
         while(scanner.hasNext()){
         
         }
         // FloatPriorityQueue.add(scanner.nextFloat());
         System.out.println(scanner.hasNext());
         }
         */

        System.out.println("取出了" + pq.poll() + ",队列剩余" + Arrays.toString(pq.toArray()));
        long endTime = System.nanoTime(); //获取结束时间  

        System.out.println("程序运行时间： " + (endTime - startTime) + "ns");
    }
}
