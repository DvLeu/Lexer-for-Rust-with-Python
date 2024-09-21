enum Color {
    Rojo,
    Verde,
    Azul,
}

struct Punto {
    x: i32,
    y: i32,
}

fn main() {
    let punto = Punto { x: 0, y: 0 };
    let color = Color::Verde;
    match color {
        Color::Rojo => println!("El color es Rojo"),
        Color::Verde => println!("El color es Verde"),
        Color::Azul => println!("El color es Azul"),
    }
}
