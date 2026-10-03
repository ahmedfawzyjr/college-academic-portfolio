// shared/data-structures/LinkedList.java
// Generic Singly Linked List Implementation in Java

public class LinkedList<T> {
    private static class Node<T> {
        T data;
        Node<T> next;
        Node(T data) {
            this.data = data;
            this.next = null;
        }
    }

    private Node<T> head;
    private int size;

    public LinkedList() {
        this.head = null;
        this.size = 0;
    }

    public void add(T element) {
        Node<T> newNode = new Node<>(element);
        if (head == null) {
            head = newNode;
        } else {
            Node<T> curr = head;
            while (curr.next != null) {
                curr = curr.next;
            }
            curr.next = newNode;
        }
        size++;
    }

    public void display() {
        Node<T> curr = head;
        System.out.print("[");
        while (curr != null) {
            System.out.print(curr.data + (curr.next != null ? " -> " : ""));
            curr = curr.next;
        }
        System.out.println("]");
    }

    public int size() { return size; }

    public static void main(String[] args) {
        LinkedList<String> list = new LinkedList<>();
        list.add("Computer");
        list.add("Science");
        list.add("Portfolio");
        list.display();
    }
}
