fn main() {
    let mut contador = 0;
    while contador < 5 {
        println!("El contador es {}", contador);
        contador += 1;
    }

    if contador == 5 {
        println!("El bucle ha terminado.");
    }
}
