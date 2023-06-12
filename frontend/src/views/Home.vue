<template>
  <div class="home">
    <div class="container main-container px-0">
      <div class="row pt-5 pb-1">
        <div class="col">
          <h3>Books API</h3>
          <img class="header-img" v-bind:src="testResponse.image_file">
        </div>
      </div>
      <div class="row py-3">
        <div class="col">
          <p>Get data on popular public domain books.</p>
        </div>
      </div>

      <div class="row py-3">
        <div class="col">
          <h5>Try it out:</h5>
        </div>
      </div>

      <div class="row input-group-desktop">
        <div class="col">
          <div class="input-group mb-3">
            <div class="input-group-prepend">
              <span class="input-group-text" id="basic-addon3">https://api.books.emshea.com/</span>
            </div>
            <input type="text" class="form-control" id="basic-url" aria-describedby="basic-addon3" v-model="testInput">
            <div class="input-group-append">
              <button class="btn btn-outline-secondary" type="button" id="button-addon2" v-on:click="getTestResponse()">Submit</button>
            </div>
          </div>
        </div>
      </div>

      <div class="row input-group-mobile">
        <div class="col">
          <div class="input-group mb-3">
            <div class="input-group-prepend px-0 col-12">
              <span class="input-group-text" id="basic-addon3">https://api.books.emshea.com/</span>
            </div>
            <input type="text" class="form-control" id="basic-url" aria-describedby="basic-addon3" v-model="testInput">
            <div class="input-group-append">
              <button class="btn btn-outline-secondary" type="button" id="button-addon2" v-on:click="getTestResponse()">Submit</button>
            </div>
          </div>
        </div>
      </div>

      <div class="row">
        <div class="col test-options">
          <p>Try
            <button class="btn btn-link test-options-btn" v-on:click="testInput = 'books/3', getTestResponse()"> books/3 </button>,
            <button class="btn btn-link test-options-btn" v-on:click="testInput = 'books/11', getTestResponse()"> books/11 </button>, or
            <button class="btn btn-link test-options-btn" v-on:click="testInput = 'books/20', getTestResponse()"> books/20 </button>.
          </p>
        </div>
      </div>

      <div class="row json">
        <div class="col scrollbar-y border mx-3">
          <tree-view :data="testResponse" :options="{maxDepth: 3, link: true}"></tree-view>
        </div>
      </div>
      <docs v-bind:books="allBooks"></docs>
      <hr>
      <div class="row">
        <div class="col footer">
          <p>Made with &hearts; by <a href="https://emshea.com">Emily</a>.</p>
        </div>
      </div>
    </div>
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
  data () {
    return {
      testInput: 'books/50',
      testUrl: null,
      testResponse: null,
      allBooks: null
    }
  },
  mounted () {
    this.getTestResponse()
    this.getBooks()
  },
  methods: {
    getTestResponse () {
      this.testResponse = 'loading...'
      this.testUrl = 'https://api.books.emshea.com/' + this.testInput
      return axios
        .get(this.testUrl, {}
        )
        .then((response) => {
          this.testResponse = response.data
        }).catch((error) => {
          this.testResponse = error.response.data
          console.log(error)
        })
    },
    getBooks () {
      this.allBooks = 'loading...'
      return axios
        .get('https://api.books.emshea.com/books', {}
        )
        .then((response) => {
          this.allBooks = response.data
        }).catch((error) => {
          this.allBooks = error.response.data
          console.log(error)
        })
    }
  }
}

</script>

<style scoped>
.header-img {
  width: 120px;
  min-height: 124.5px;
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
