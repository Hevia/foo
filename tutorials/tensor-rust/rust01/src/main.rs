fn main() {
    let xs: [i32; 5] = [1, 2, 3, 4, 5];
    let ys =  &xs[2..4];
    
    println!("xs: {:?}", xs[2]);
    println!("ys: {:?}", ys[0]);
    // xs[2] = 4;
    println!("xs: {:?}", xs[2]);
    println!("ys: {:?}", ys[0]);
}
