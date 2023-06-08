<template>
  <div class="home">
  </div>
</template>

<script>
// @ is an alias to /src
import docs from '@/components/docs.vue'

export default {
  name: 'Home',
  components: {
    docs
  },
  data () {},
  mounted () {},
  methods: {}
}

</script>

<style scoped>
.header-img {
  width: 40px;
}
:hover.header-img {
  cursor: pointer;
}
.cat-img {
  width: 40px;
}
.json {
  text-align: left;
}
.scrollbar-y {
  max-height: 212px;
  overflow-y: auto;
}
.footer {
  text-align: left;
}
.test-options {
  text-align: left;
}
.test-options-btn {
  padding: 0;
  border: none;
  vertical-align: baseline;
}
.input-group-mobile .input-group-text {
  width: 100%
}
.input-group-mobile {
    visibility: hidden;
    display: none;
}
.main-container {
  max-width: 50%;
}
@media(max-width:767px){
  .main-container {
    max-width: 80%;
  }
}
@media(max-width:1000px){
  .input-group-desktop {
    visibility: hidden;
    display: none;
  }
  .input-group-mobile {
    visibility: visible;
    display: flex;
  }
}
</style>
