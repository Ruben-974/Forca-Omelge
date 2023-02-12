const randrange = require("random").randrange;

const forca = (escolhida, censura, chances, resp) => {
  if (chances === 0) {
    console.log(
      `Você perdeu :(\nA palavra era: ${escolhida.join("")}`
    );
    return [false, chances];
  }
  if (escolhida.includes(resp) && resp.length === 1) {
    for (let c = 0; c < escolhida.length; c++) {
      if (resp === escolhida[c]) {
        censura[c] = resp;
      }
    }
    if (!censura.includes("_")) {
      console.log(
        `Forca: ${censura.join(" ")} | ${chances} Chances (Sem dica!)`
      );
      console.log(`Parabéns você acertou :D`);
      return [false, chances];
    } else {
      return [true, chances];
    }
  }
  if (resp === escolhida.join("") || !censura.includes("_")) {
    console.log(`Parabéns você acertou :D`);
    return [false, chances];
  } else {
    chances -= 1;
    return [true, chances];
  }
};

const palavras = [
  "Árvore",
  "Girassol",
  "Balanço",
  "Computador",
  "Caminhão",
  "Elefante",
  "Livro",
  "Girafa",
  "Refrigerador",
  "Bolsa",
  "Cachorro",
  "Gato",
  "Avião",
  "Bicicleta",
  "Casa",
  "Banheiro",
  "Cozinha",
  "Jardim",
  "Carro",
  "Chave"
];
let chances = 5;
let continuar = true;

const escolhida = palavras[randrange(palavras.length)].split("");
const censura = new Array(escolhida.length).fill("_");

console.log(
  `Olá, sou o bot da forca, vamos jogar?\nEscreva uma letra ou uma palavra desejada, mas tenha cuidado! Suas chances diminuem a cada erro!\nBOA SORTE!`
);

while (continuar) {
  console.log(`Forca: ${censura.join(" ")} | ${chances} Chances (Sem dica!)`);

  const resp = prompt(`Digite uma letra: `).toUpperCase();

  [continuar, chances] = forca(escolhida, censura, chances, resp);
}

console.log(
  `Se você quiser incentivar/ajudar meu desenvolvedor o chave pix dele é: e0b2c13a-8b11-4871-9a93-cda
