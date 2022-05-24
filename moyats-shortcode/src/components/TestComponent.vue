<template>

  <div id="test-buttons">
    <h3>{{ num }}</h3>
    <a @click="num++">+</a>    <a @click="num--">-</a>
  </div>

</template>

<script>
export default {
  props: {
    facebook: { type: Boolean, default: true },
    twitter: { type: Boolean, default: true },
    gplus: { type: Boolean, default: true }
  },
  data:()=>({
    num:0,
  }),
  methods: {
    share ($event) {
      window.alert('Share on ' + $event.target.innerHTML);
    }
  }
}
</script>

<style scoped>
  #test-buttons a {
    display: inline-block;
    border: 1px solid #ddd;
    padding: 10px 20px;
    margin-right: 10px;
    text-transform: uppercase;
    color: #999;
    text-decoration: none;
  }
  #test-buttons a:hover {
    color: #333;
    border-color: #888;
  }
</style>
