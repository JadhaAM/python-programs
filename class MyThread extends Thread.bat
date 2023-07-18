class MyThread extends Thread
{
    public void run()
    {
        system.out.printin("thread is created!!!")
    }
}
class ThreadProg
{
    public static void main(string args[])
    {
        MyThread t=new MyThread();
        t.start();
    }
}