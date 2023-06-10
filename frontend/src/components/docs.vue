<template>
    <div id="docs">
      <div class="row pt-5 pb-1">
          <div class="col">
              <h4>Documentation</h4>
          </div>
      </div>
      <div class="row">
          <div class="col docs-subheader">
              <h5><a href='#overview' id='overview' class="anchor-link">Overview</a></h5>
              <p>Use this API to get data on popular public domain books.</p>
              <p>Data for this API is sourced from <a href="https://www.gutenberg.org/">Project Gutenberg</a> via the <a href="gutendex.com">Gutendex API</a>. This API is rate limited at 120 API requests per minute.</p>
              <!-- <ul>
                <li><a href="#books">Books</a></li>
                <li><a href="#authors">Authors</a></li>
              </ul> -->
          </div>
      </div>
      <hr>
      <div class="row">
        <div class="col docs-subheader">
            <h5><a href='#books' id='books' class="anchor-link">Books</a></h5>
            <p>Returns data on books.</p>
            <h6> GET /books </h6>
            <p> This endpoint lists all books.</p>
            <div class="row json">
                <div class="col scrollbar-y border mx-3 mb-3">
                    <tree-view :data="books" :options="{maxDepth: 3, link: true}"></tree-view>
                </div>
            </div>
            <h6>GET /books/{id}</h6>
            <p> This endpoint returns a book for a given id. Valid ids are between 1-60. Names are not case sensitive.</p>
            <div class="row json">
                <div class="col scrollbar-y border mx-3 mb-3">
                    <tree-view :data="exampleBookResponse" :options="{maxDepth: 3, link: true}"></tree-view>
                </div>
            </div>
            <h6>Book resource definition</h6>
            <div class="row table-row pb-3">
              <div class="col table-col">
                <table class="table table-responsive-md table-bordered">
                  <thead>
                    <tr>
                      <th scope="col">Name</th>
                      <th scope="col">Description</th>
                      <th scope="col">Example</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="item in bookDataModel" :key="item.Id">
                      <td>{{ item.Name }}</td>
                      <td>{{ item.Description }}</td>
                      <td>{{ item.Example }}</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
          </div>
      </div>
    </div>
</template>

<script>
export default {
  name: 'docs',
  props: ['books'],
  data () {
    return {
      bookDataModel: [
        { Name: 'book_id', Description: 'Id number of book (1-60)', Example: '17', Id: '1' },
        { Name: 'title', Description: 'Name of cat', Example: 'The Count of Monte Cristo', Id: '2' },
        { Name: 'author_first_name', Description: "Book author's first name", Example: 'Alexandre', Id: '3' },
        { Name: 'author_last_name', Description: "Book author's last name", Example: 'Dumas', Id: '4' },
        { Name: 'image_file', Description: 'Link to book cover image file', Example: 'https://books-api-images.s3.amazonaws.com/book-pink.png', Id: '5' }
      ]
    }
  },
  mounted () {
  },
  methods: {
  },
  computed: {
    exampleBookResponse: function () {
      if (this.books === null) {
        return 'loading...'
      } else if (typeof this.books === 'string') {
        return this.books
      } else {
        return this.books[16]
      }
    }
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
