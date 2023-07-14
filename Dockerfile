    #AQUI TIENE QUE IR LA IMAGEN QUE LA BUSCAREMOS EN EL DOCKER HUB
    FROM node:20-alpine3.17

    #declaramos las variable de entorno para utilizar en esta imagen
    ENV PORT=8000
    ENV NOMBRE=Erick

    #que la imagen almacene de manera mas facil los archivos del proyecyo porque al indicar la ubicaciopn del dicretorio de trabajo creara una carpeta en la imagen donde guardara todos los archivos copiados

    WORKDIR /app

    #ahora copiamos los archivos locales a nuesta imagen
    #el nombre del archivo o directorio | en donde o como se llamara la imagen
    COPY package.json package.json

    # o tambien se puede copiar de la siguiente manera
    # las primeras posiciones seral los archivos a copiar y la ultima posicion hacia donde se va a copiar, no es necesario volver a poner "/app" ya que ese sera el directirio por defecto
    COPY ["package-lock.json",".","./"]

    # se usa pra instalar las librerias
    # --producttion > sirve para solamente instalar las dependencias y no las de desarrollo
    RUN npm install --production

    CMD ["npm","start"]