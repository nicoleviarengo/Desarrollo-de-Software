<template>
    <div class="cuadro">
      <h1>{{ name }}</h1>
    </div>
</template>

<script>
/* eslint-disable */
export default {
    name: 'Cuadro',
    props: [
      "name", 
    ]
}
</script>

<style>
.cuadro{
  width: 300px;
  height: 400px;
  background-color: white;
  margin: 15px;
}
h1 {
  color: black;
}
</style>