<template>
    <div id="cargar">
      <head>
        <link href="https://fonts.googleapis.com/css?family=Inter&display=swap" />
    </head>
    <body>
        <div class="v3_15">
            <div class="v1_3">
              <button class="boton-guardar" @click="Guardar()">Guardar</button>
            </div>
            <div class="linea"></div>
            <span class="v1_4">Cargar Cuadro</span>
            <span class="nombre">Nombre: </span>
            <input class='nombre-v' v-model="name">
            <span class="fecha">Fecha</span>
            <input class="fecha-v" v-model="date">
            <span class="precio">Precio</span>
            <input class="precio-v" v-model="price">
            <span class="imagen">Imagen</span>
            <input class="imagen-v" v-model="image">
            <router-link to="/" class="boton-salir" >Salir</router-link>
          <router-view />
          </div>
    </body>
    </div>
</template>

<script>
/* eslint-disable */
import axios from 'axios'

export default {
  name: 'Cargar',
  data: function(){
    return {
      name: null,
      date: null,
      price: 0,
      image: null
    }
  },
  methods: {
        cargarCuadros (){
            axios.get('http://127.0.0.1:8000/')
            .then(response => {
                this.cuadros = response.data
                console.log(response.data)
            })
            .catch(error => {
                console.log(error)
            })
        },
    },
    Guardar(){
            axios.post('http://127.0.0.1:8000/', {
                name: this.name,
                price: this.price,
                date: this.date,
                image: this.image
            })
            .then(response => {
                console.log(response)
                this.cargarCuadros()
            })
            .catch(error => {
                console.log(error)
            })
        },
    mounted() {
        this.cargarCuadros()
    }
}

</script>

<style>
* {
  box-sizing: border-box;
}
body {
  font-size: 14px;
}
.v3_15 {
  width: 100%;
  height: 1024px;
  background: rgba(255,255,255,1);
  opacity: 1;
  position: relative;
  top: 0px;
  left: 0px;
  overflow: hidden;
}
.v1_3 {
  margin-left: -50px;
  margin-top: -40px;
  width: 717px;
  height: 348px;
  background: rgba(230,224,233,1);
  opacity: 1;
  position: absolute;
  top: 500px;
  left: 350px;
  border: 1px solid rgba(0,0,0,0.25999999046325684);
}

.boton-guardar {
  position: absolute;
  margin-top: 52%;
  margin-left: 40%;
  padding-top: 2%;
  padding-bottom: 2%;
  padding-left: 5%;
  padding-right: 5%;
  font-size: 0.5cm;
  border-color: rgb(78, 77, 77);
  border-radius: 5px;
  background-color: rgb(171, 104, 233);
}
.boton-guardar:hover {
  background-color:rgb(215, 181, 245);
  cursor: pointer;
}

.linea {
  margin-right: 405px;
  margin-left: 405px;
  width: 500px;
  height: 1px;
  opacity: 1;
  position: absolute;
  top: 162px;
  border: 1px solid rgba(0,0,0,1);
}
.v1_4 {
  width: 170px;
  color: rgba(74,73,73,1);
  position: absolute;
  top: 123px;
  left: 403px;
  font-family: Inter;
  font-weight: Semi Bold;
  font-size: 24px;
  opacity: 1;
  text-align: left;
}
.nombre {
  width: 87px;
  color: rgba(74,73,73,1);
  position: absolute;
  top: 206px;
  left: 403px;
  font-family: Inter;
  font-weight: Regular;
  font-size: 20px;
  opacity: 1;
  text-align: left;
}

.nombre-v {
  position: absolute;
  top: 210px;
  left: 515px;
}

.fecha {
  width: 86px;
  color: rgba(74,73,73,1);
  position: absolute;
  top: 252px;
  left: 402px;
  font-family: Inter;
  font-weight: Regular;
  font-size: 20px;
  opacity: 1;
  text-align: left;
}
.fecha-v {
  position: absolute;
  top: 255px;
  left: 515px;
}

.precio {
  width: 72px;
  color: rgba(74,73,73,1);
  position: absolute;
  top: 295px;
  left: 402px;
  font-family: Inter;
  font-weight: Regular;
  font-size: 20px;
  opacity: 1;
  text-align: left;
}
.precio-v {
  position: absolute;
  top: 298px;
  left: 515px;
}

.imagen {
  width: 75px;
  color: rgba(74,73,73,1);
  position: absolute;
  top: 341px;
  left: 400px;
  font-family: Inter;
  font-weight: Regular;
  font-size: 20px;
  opacity: 1;
  text-align: left;
}

.imagen-v {
  position: absolute;
  top: 345px;
  left: 515px;
}

.boton-salir {
  position: absolute;
  margin-top: 35%;
  margin-left: 68%;
  padding: 4px;
  font-size: 0.5cm;
  border-color: rgb(78, 77, 77);
  border-radius: 5px;
  background-color: rgb(171, 104, 233);
}
.boton-salir:hover {
  background-color: rgb(235, 220, 248);
}
</style>