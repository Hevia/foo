
fn main() {
    let mut arguments = std::env::args().skip(1);
    let key = arguments.next().unwrap();
    let value = arguments.next().unwrap();
    let write_result = write_database(key, value);
    match write_result {
        Ok(()) => {println!("Wrote file successly")},
        Err(err_msg) => {println!("Error when writing file: {}", err_msg)}
    }
}

fn write_database(key: String, value: String) -> Result<(), std::io::Error> {
    let content = format!("{} {}", key, value);
    return std::fs::write("kv.db", "some file contents");
}





































