// Importar librería necesaria
#include <cvzone.h>

// Indicar que se pasará 1 elemento de 1 dígito por el puerto serial
SerialData serialData(1,1);

// Declarar la variable que guardará el dígito que envié el puerto
int valsRec[1];

// Función de iniciación
void setup() {
  // Iniciar el puerto serial
  serialData.begin();
  // Habilitar el pin 13 como salida
  pinMode(13,OUTPUT);
}

// Función para iterar el algoritmo del programa
void loop() {
  // Obtener el digito que recibe el puerto
  serialData.Get(valsRec);
  // Enviar al pin 13 el digito recibido 
  digitalWrite(13,valsRec[0]);
}
