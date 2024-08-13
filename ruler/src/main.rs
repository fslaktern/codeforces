use std::io;

fn main() {
    let mut num_tests_buf = String::new();
    let stdin = io::stdin();
    stdin.read_line(&mut num_tests_buf)
        .expect("Couldn't read line from stdin");
    let num_tests = num_tests_buf.trim().parse::<u32>()
        .expect("Failed converting number of tests to u32");

    for _ in 0..num_tests {
        let mut lo = 1;
        let mut hi = 999;
        let mut m1 = lo + (hi - lo) / 3;
        let mut m2 = lo + 2 * (hi - lo) / 3;
        
        loop {
            println!("? {m1} {m2}");

            let mut jury_buf = String::new();
            stdin.read_line(&mut jury_buf)
                .unwrap();
            let jury = jury_buf
                .trim()
                .parse::<u32>()
                .unwrap();
            
            if jury == m1 * m2 {  
                // println!("# {a} {b} {c} {d} (above)");
                if m2 - m1 <= 1 && hi - m2 <= 1 {
                    println!("! {hi}");
                    break;
                }
                lo = m2 + 1;
                m1 = lo + (hi - lo) / 3;
                m2 = lo + 2 * (hi - lo) / 3;
            } else if jury == m1 * (m2 + 1) {
                // println!("# {a} {b} {c} {d} (middle)");
                if m2 - m1 <= 1 {
                    println!("! {m2}");
                    break
                } else if m2 - m1 == 2 {
                    (lo, hi) = (m1, m2);
                    m2 -= 1;
                } else {
                    (lo, hi) = (m1 + 1, m2);
                    m1 = lo + (hi - lo) / 3;
                    m2 = lo + 2 * (hi - lo) / 3;
                }
            } else if jury == (m1 + 1) * (m2 + 1) {
                // println!("# {a} {b} {c} {d} (below)");
                if hi - lo <= 1 {
                    println!("! {m1}");
                    break
                }
                hi = m1;
                m1 = lo + (hi - lo) / 3;
                m2 = lo + 2 * (hi - lo) / 3;
            }
        }
    }
}
