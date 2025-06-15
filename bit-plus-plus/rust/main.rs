use std::io;

fn main() {
    let mut x: i16 = 0;
    let mut input_n = String::new();

    io::stdin().read_line(&mut input_n).expect("Failed to read line");
    let mut n: u8 = input_n.trim().parse().expect("Failed parsing `n` as u8");
    assert!(n <= 150);

    while n > 0 {
        let mut input_op = String::new();
        io::stdin().read_line(&mut input_op).expect("Failed to read line");
        let op = input_op.chars().nth(1).expect("Line is not long enough to be properly parsed");
        if op == '+' {
            x += 1;
        } else {
            x -= 1;
        }
        n -= 1;
    }
    println!("{}", x);
}
