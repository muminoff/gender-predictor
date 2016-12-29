<template>
  <div class="hello">
    <form>
      <div class="row">
        <div class="columns">
          <input type="text" placeholder="Исм" autofocus required>
        </div>
      </div>
    </form>
  </div>
</template>

<script>
export default {
  name: 'hello',
  data () {
    return {
      msg: 'Жинсни аниқлаш'
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
input {
  font-weight: normal;
  font-family: 'Merriweather', serif;
  border-color: none;
  height: 60px;
  font-size: 40px;
}

input :hover :focus {
  border: none;
}
</style>
