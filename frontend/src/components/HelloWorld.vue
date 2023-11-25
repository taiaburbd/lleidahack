<template>
  <div class="hero_area">
    <div class="hero-bg">
      <img src="images/hero-bg.jpg" alt="">
    </div>
    <!-- header section strats -->
    <header class="header_section">
      <div class="container">
        <nav class="navbar navbar-expand-lg custom_nav-container ">
          <a class="navbar-brand" href="/">
            <span>
              Plant-projects
            </span>
          </a>

          <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class=""> </span>
          </button>

          <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav  ">
              <li class="nav-item active">
                <a class="nav-link" href="/">Home <span class="sr-only">(current)</span></a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#about"> About</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#ourplants">Plant Info</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#why_section">Why we are</a>
              </li>

            </ul>
          </div>
        </nav>
      </div>
    </header>
    <!-- end header section -->
    <!-- slider section -->
    <section class="slider_section ">
      <div id="customCarousel1" class="carousel slide" data-ride="carousel">
        <div class="carousel-inner">
          <div class="carousel-item active">
            <div class="container ">
              <div class="row">
                <div class="col-md-7 col-lg-6 mx-auto ">
                  <div class="detail-box">
                    <h1>
                      Make Your House Alive
                    </h1>
                    <p>
                      Explicabo esse amet tempora quibusdam laudantium, laborum eaque magnam fugiat hic? Esse dicta aliquid error repudiandae earum suscipit fugiat molestias, veniam, vel architecto veritatis delectus repellat modi impedit sequi.
                    </p>
                    <div class="btn-box">
                      <a href="" class="btn1">
                        Order Now
                      </a>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="carousel-item ">
            <div class="container ">
              <div class="row">
                <div class="col-md-7 col-lg-6 mx-auto ">
                  <div class="detail-box">
                    <h1>
                      Make Your House Alive
                    </h1>
                    <p>
                      Explicabo esse amet tempora quibusdam laudantium, laborum eaque magnam fugiat hic? Esse dicta aliquid error repudiandae earum suscipit fugiat molestias, veniam, vel architecto veritatis delectus repellat modi impedit sequi.
                    </p>
                    <div class="btn-box">
                      <a href="" class="btn1">
                        Order Now
                      </a>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="carousel-item">
            <div class="container ">
              <div class="row">
                <div class="col-md-7 col-lg-6 mx-auto ">
                  <div class="detail-box">
                    <h1>
                      Make Your House Alive
                    </h1>
                    <p>
                      Explicabo esse amet tempora quibusdam laudantium, laborum eaque magnam fugiat hic? Esse dicta aliquid error repudiandae earum suscipit fugiat molestias, veniam, vel architecto veritatis delectus repellat modi impedit sequi.
                    </p>
                    <div class="btn-box">
                      <a href="" class="btn1">
                        Order Now
                      </a>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="container">
          <ol class="carousel-indicators">
            <li data-target="#customCarousel1" data-slide-to="0" class="active"></li>
            <li data-target="#customCarousel1" data-slide-to="1"></li>
            <li data-target="#customCarousel1" data-slide-to="2"></li>
          </ol>
        </div>
      </div>

    </section>
    <!-- end slider section -->
  </div>

  <!-- plant section -->
 
  <section id="ourplants" class="plant_section layout_padding">
    <div class="container">
      <div class="heading_container heading_center">
        <h2>
          Our <span>plants</span>
        </h2>
      </div>
      <div class="row">
        <div v-for="(index, item) in data" :key="index" class="col-sm-6 col-md-4 col-lg-3" @click="toggleDiv(index)">
          <div class="box" >
            <div class="img-box">
              <img :src="'images/p' + (item+1) + '.png'" alt="">
            </div>
            <div class="detail-box">
              <a href="#">
                {{index}}
              </a>
            </div>
          </div>
        </div>
        <div v-if="isDivVisible" class="col-md-12">
        <div class="col-md-3">
          <p>Plant Summary: </p>
          <table class="table table-sm" >
            <tr>
              <th>item</th>
              <th>value</th>
            </tr>
            <tr v-for="(index,item) in summary" :key="index">
              <td>{{ item}}</td>
              <td v-if="item=='ts'">{{ formatTimestamp(index) }}</td>
              <td v-else>{{ index }}</td>
            </tr>
          </table>
            <h6 >{{ item }} <span class="badge bg-warning">{{ index}}</span></h6>
            <button class="btn btn-info" @click="toggleDivDetails()">Show details</button>
        </div>
        <div v-if="isDivVisibleDetails" class="col-md-6">
          <p>Plant Details: <br/>
          <table class="table table-sm table-striped">
            <tr>
              <th>timestamp</th>
              <th>temperature</th>
              <th>humidity</th>
              <th>airHumidity</th>
              <th>light</th>
            </tr>
            <tr v-for="(index) in detail" :key="index">
              <td>{{ formatTimestamp(index.ts) }}</td>
              <td>{{ index.temperature }}</td>
              <td>{{ index.humidity }}</td>
              <td>{{ index.airHumidity }}</td>
              <td>{{ index.light }}</td>
            </tr>
          </table>
          </p>
        </div>
      </div>
      </div>
    </div>
  </section>

  <!-- end plant section -->

  <!-- about section -->

  <section id="about" class="about_section layout_padding-bottom">
    <div class="container  ">
      <div class="row">
        <div class="col-md-6 ">
          <div class="img-box">
            <img src="images/about-img.jpg" alt="">
          </div>
        </div>
        <div class="col-md-6">
          <div class="detail-box">
            <div class="heading_container">
              <h2>
                About <span>Us</span>
              </h2>
            </div>
            <p>
              There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration
              in some form, by injected humour, or randomised words which don't look even slightly believable. If you
              are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in
              the middle of text. All
            </p>
            <!-- <a href="">
              Read More
            </a> -->
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- end about section -->

  <!-- why section -->

  <section id="why_section" class="why_section layout_padding">
    <div class="container">
      <div class="heading_container heading_center">
        <h2>
          Why Choose <span>Us</span>
        </h2>
      </div>
      <div class="row">
        <div class="col-md-6 mx-auto">
          <div class="box">
            <div class="img-box">
              <img src="images/w1.png" alt="">
            </div>
            <div class="detail-box">
              <h5>
                Free Delivery
              </h5>
              <p>
                Nihil molestiae non culpa dignissimos dolorem, facere amet reiciendis esse nulla ut aperiam voluptate ipsum nemo temporibus inventore hic accusantium nesciunt vero iste odit
              </p>
            </div>
          </div>
        </div>
        <div class="col-md-6 mx-auto">
          <div class="box">
            <div class="img-box">
              <img src="images/w2.png" alt="">
            </div>
            <div class="detail-box">
              <h5>
                Safe Payment
              </h5>
              <p>
                Nihil molestiae non culpa dignissimos dolorem, facere amet reiciendis esse nulla ut aperiam voluptate ipsum nemo temporibus inventore hic accusantium nesciunt vero iste odit
              </p>
            </div>
          </div>
        </div>
        <div class="col-md-6 mx-auto">
          <div class="box">
            <div class="img-box">
              <img src="images/w3.png" alt="">
            </div>
            <div class="detail-box">
              <h5>
                Satisfied Customers
              </h5>
              <p>
                Nihil molestiae non culpa dignissimos dolorem, facere amet reiciendis esse nulla ut aperiam voluptate ipsum nemo temporibus inventore hic accusantium nesciunt vero iste odit
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- end why section -->

  <!-- client section -->

  <section class="client_section layout_padding-bottom">
    <div class="container">
      <div class="heading_container heading_center psudo_white_primary mb_45">
        <h2>
          What Says Our <span>Customers</span>
        </h2>
      </div>
      <div class="carousel-wrap row ">
        <div class="owl-carousel client_owl-carousel">
          <div class="item">
            <div class="box">
              <div class="img-box">
                <img src="images/client1.jpg" alt="" class="box-img">
              </div>
              <div class="detail-box">
                <p>
                  Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam
                </p>
                <h6>
                  Adam Miller
                </h6>
                <p>
                  magna aliqua
                </p>
              </div>
            </div>
          </div>
          <div class="item">
            <div class="box">
              <div class="img-box">
                <img src="images/client2.jpg" alt="" class="box-img">
              </div>
              <div class="detail-box">
                <p>
                  Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam
                </p>
                <h6>
                  Lily James
                </h6>
                <p>
                  magna aliqua
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- end client section -->


  <!-- footer section -->
  <footer class="footer_section">
    <div class="container">
      <a href="" class="footer-brand">
        Plants-Project
      </a>

    </div>
    <div class="footer-info">
      <div class="container">
        <p>
          &copy; <span id="displayYear"></span> All Rights Reserved By
          <a href="">Free Html Templates</a>
        </p>
      </div>
    </div>
  </footer>
  
</template>

<script>
import axios from 'axios';

export default {
  name: 'HelloWorld',
  props: {
    msg: String
  },
  data() {
    return {
      data: null,
      plantDetails: '',
      isDivVisible: false,
      isDivVisibleDetails: false,
      activePlant:false,
      summary: {},
      detail:{},
    };
  },
  created() {
    this.fetchData();
  },
  methods: {
    formatTimestamp(timestamp) {
      const date = new Date(timestamp);
      const year = date.getFullYear();
      const month = (date.getMonth() + 1).toString().padStart(2, '0');
      const day = date.getDate().toString().padStart(2, '0');
      const hours = date.getHours().toString().padStart(2, '0');
      const minutes = date.getMinutes().toString().padStart(2, '0');
      const seconds = date.getSeconds().toString().padStart(2, '0');

      return `${year}-${month}-${day} ${hours}:${minutes}:${seconds}`;
    },
    toggleDiv(plant) {

      axios.get('http://127.0.0.1:5000/plant/'+plant+'/summary')
      .then(response => {
        // Handle the successful response
        this.summary=response.data;
        this.activePlant=plant;
      })
      .catch(error => {
        // Handle the error
        console.error('Error fetching data:', error.message);
      });
      this.isDivVisible = !this.isDivVisible;
    },
    toggleDivDetails() {
      axios.get('http://127.0.0.1:5000/plant/'+this.activePlant+'/detail')
      .then(response => {
        // Handle the successful response
        this.detail=response.data;
        console.log(response.data);
      })
      .catch(error => {
        // Handle the error
        console.error('Error fetching data:', error.message);
      });
      this.isDivVisibleDetails = !this.isDivVisibleDetails;
    },
    
    fetchData() {
      axios.get('http://127.0.0.1:5000/plants')
        .then(response => {
          // Handle the successful response
          this.data = response.data;
        })
        .catch(error => {
          // Handle errors
          console.error('Error fetching data:', error);
        });
    },
  },
};
</script>
