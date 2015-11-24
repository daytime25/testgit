/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package congtaozailai;

import java.io.*;

import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.Random;
import java.util.Scanner;

/**
 *
 * @author ming
 */
public class PriorityQueueTest1 {

    /* public static void PrintPr(Queue<!--?--> queue){
     while(queue.peek()!=null){
     System.out.print(queue.remove()+" ");
     }
     System.out.println();
     }*/
    public static void main(String[] args) throws FileNotFoundException, IOException {

        long startTime = System.nanoTime();

        /*FileReader fr=new FileReader("/javaPro/congtaozailai/input.txt");
         BufferedReader bf=new BufferedReader(fr);*/
        Scanner scanner = new Scanner(new File("/javaPro/congtaozailai/input.txt"));
        Queue FloatPriorityQueue = new PriorityQueue<>();
        while (scanner.hasNextFloat()) {
            String str = scanner.nextLine();

            System.out.println(str);
            FloatPriorityQueue.add(str);
            System.out.println("Processing Integer:" + FloatPriorityQueue.poll());
        }
        System.out.println("-----------------------------");
       // System.out.println(scanner.nextFloat());
        //优先队列自然排序示例
        //Queue<Float> FloatPriorityQueue = new PriorityQueue<>(7);
        //Random rand = new Random();
        //flag = Integer.parseInt(flag1);  //flag1为null，就会报你说的错误
       /* for (int i = 0; i < 100000; i++) {
         FloatPriorityQueue.add(new Float(bf.readLine()));
         }
         for (int i = 0; i < 200; i++) {
         //Float in = FloatPriorityQueue.poll();
         System.out.println("Processing Integer:" + FloatPriorityQueue.poll());
         }*/
        //优先队列使用示例
        Queue<Customer> customerPriorityQueue = new PriorityQueue<>(200, idComparator);
        addDataToQueue(customerPriorityQueue);

        pollDataFromQueue(customerPriorityQueue);

        long endTime = System.nanoTime(); //获取结束时间  

        System.out.println("程序运行时间： " + (endTime - startTime) + "ns");
    }

    //匿名Comparator实现
    public static Comparator<Customer> idComparator = new Comparator<Customer>() {

        @Override
        public int compare(Customer c1, Customer c2) {
            return (int) (c1.getId() - c2.getId());
        }
    };

    //用于往队列增加数据的通用方法
    private static void addDataToQueue(Queue<Customer> customerPriorityQueue) {
        Random rand = new Random();
        for (int i = 0; i < 200; i++) {
            int id = rand.nextInt(200);
            customerPriorityQueue.add(new Customer(id, "Pankaj " + id));
        }
    }

    //用于从队列取数据的通用方法
    private static void pollDataFromQueue(Queue<Customer> customerPriorityQueue) {
        while (true) {
            Customer cust = customerPriorityQueue.poll();
            if (cust == null) {
                break;
            }
            System.out.println("Processing Customer with ID=" + cust.getId());
        }
    }

}
