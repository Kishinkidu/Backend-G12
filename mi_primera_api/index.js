import esImpar from 'is-odd-num'

let resultado = esImpar(10)

console.log(resultado)

const miCalculoImpar =(numero) =>{
    if (numero%2 ===0 ){
        return false
    } else {
        return true
    }

}

resultado = miCalculoImpar(10)

//operador ternario
// condicion ? VERDADERA : FALSE
console.log(resultado === true? "es impar": "Es par")

//operador AND &&
//si la primera condicion es true ono es null o undefined pasara a la segunda expresion
// se utiliza si queremos validar si la condicion solamente es verdadera osea no terner un else
console.log(resultado === false && "otra cosa")

//operador OR
// si la primera expresion es verdadera se quedara ahi peros si es falsa, null o undefined pasara a la segunda 
console.log(resultado === 0 || "Otra Cosa")

//operador Nullish coalescing operator??
// es un operador logico que retornara lo del a derecha si la parte de la izquierda es null o undifined de otra manera retornara lo de la izquierda
// el caracter 0 indica nulidad en js
console.log(0 ?? "otra cosa")