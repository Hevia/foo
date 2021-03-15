#[derive(Debug)]

struct Object {
    width: u32,
    height: u32,
}

impl Object {
    fn area(&self) -> u32 {
        self.width * self.height
    }

    fn new(width: u32, height: u32) -> Object {
        Object {
            width,
            height,
        }
    }
}

fn main() {
    let o = Object::new(32, 32);

    println!("{:?}", o.area());
}
