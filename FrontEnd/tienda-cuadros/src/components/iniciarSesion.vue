<template>
  <div>
    <form @submit.prevent="login">
      <head>
        <link href="https://fonts.googleapis.com/css?family=Inter&display=swap" />
    </head>
    <body>
        <div class="v1_2">
            <div class="v1_3"></div>
            <span class="iniciar">Iniciar Sesion</span>
            <div class="linea"></div>
            <label for="username" class="usuario">Usuario:</label>
            <input class="barra-user" type="text" id="username" v-model="username" />
            <label for="password" class="contra">Contraseña:</label>
            <input class="barra-pass" type="password" id="password" v-model="password"/>
            <!-- <button class="boton-ingresar" type="submit">Ingresar</button>-->
            <!--me inicia igual aunq los datos sean incorrectos-->
            <router-link to="/">Home</router-link>
            <router-link to="/cargarCuadros" class="boton-ingresar">Ingresar</router-link>
            <router-view />
        </div>
    </body>
    </form>
  </div>
</template>

<script>
/* eslint-disable */

export default {
    name: 'Inicio',
    data: function() {
        return {
            username: ' ',
            password: ' '
        }
    },
    methods: {
    Ingresar() {
      if (this.username === "usuario" && this.password === "contraseña") {
        // Usuario autenticado con éxito, redirige a la página Cargar
        this.$router.push("/");
      } else {
        console.log("Inicio de sesión fallido");
      }
    },
  },
}

</script>

<style>
* {
  box-sizing: border-box;
}
body {
  font-size: 14px;
}
.v1_2 {
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
  width: 603px;
  height: 415px;
  background: rgba(231,225,234,1);
  opacity: 1;
  position: absolute;
  top: 132px;
  left: 418px;
  border: 1px solid rgba(0,0,0,0.25999999046325684);
  overflow: hidden;
}
.iniciar {
  width: 253px;
  color: rgba(74,73,73,1);
  position: absolute;
  top: 120px;
  left: 400px;
  font-family: Inter;
  font-weight: Regular;
  font-size: 32px;
  opacity: 1;
  text-align: left;
}
.linea {
  margin-right: 405px;
  margin-left: 395px;
  width: 500px;
  height: 1px;
  opacity: 1;
  position: absolute;
  top: 170px;
  border: 1px solid rgba(0,0,0,1);
}
.usuario {
  width: 281px;
  color: rgba(74,73,73,1);
  position: absolute;
  top: 224px;
  left: 400px;
  font-family: Inter;
  font-weight: Regular;
  font-size: 32px;
  opacity: 1;
  text-align: left;
}
.barra-user {
  position: absolute;
  top: 235px;
  left: 520px;
}
.contra {
  width: 242px;
  color: rgba(74,73,73,1);
  position: absolute;
  top: 288px;
  left: 400px;
  font-family: Inter;
  font-weight: Regular;
  font-size: 32px;
  opacity: 1;
  text-align: left;
}
.barra-pass {
  position: absolute;
  top: 299px;
  left: 570px;
}
.boton-ingresar {
  position: absolute;
  margin-top: 30%;
  margin-left: 41%;
  padding-top: 1.5%;
  padding-bottom: 1.5%;
  padding-left: 4%;
  padding-right: 4%;
  font-size: 0.5cm;
  border-color: rgb(78, 77, 77);
  border-radius: 5px;
  background-color: rgb(171, 104, 233);
}
.boton-ingresar:hover {
  background-color: rgb(215, 181, 245);
  cursor: pointer;
}
</style>