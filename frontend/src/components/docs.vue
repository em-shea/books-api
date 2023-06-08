<template>
    <div id="docs">
    </div>
</template>

<script>
export default {
  name: 'docs',
  props: [],
  data () {
  },
  mounted () {
  },
  methods: {
  },
  computed: {

  }
}
</script>

<style scoped>
.docs-subheader {
  text-align: left;
}
.docs-subheader .anchor-link {
  color: black;
}
.scrollbar-y {
  max-height: 212px;
  overflow-y: auto;
}
.row .table {
  width: unset;
}
@media(max-width:767px){
  .table {
    font-size: 13px;
  }
}
</style>
