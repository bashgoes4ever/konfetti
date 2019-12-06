<template>
  <div>
    <section class="block1"><img src="img/block1/bg.png" alt="" class="block__bg block1__bg"/>
      <div class="container">
        <h1>Создадим атмосферу <br>вашего праздника <br>и сделаем его <br>незабываемым!</h1>
        <div class="block1__descriptor">Офоормление праздников воздушными шарами, <br>декорирование и праздничные товары</div>
      </div>
    </section>
    <section class="block2">
      <div class="container"><img src="img/block2/bg1.png" alt="" class="block2__img1"/><img src="img/block2/bg2.png" alt="" class="block2__img2"/>
        <h2 class="section__title"> <span class="title">Популярные темы
						<div class="before"></div>
						<div class="after"></div></span></h2>
        <div class="block2__flex" v-if="block2.length != 0">

          <router-link :to="`/${item.section.slug}?category=${item.id}`" class="block2__item" v-for="item in block2" :key="item.id">
            <div :style="`background-image: url(http://127.0.0.1:8000/${item.image_thumb})`" class="block2__item__img"></div>
            <div class="block2__item__text">
              <div class="title">{{item.title}}</div>
              <div class="text">{{item.description}}</div>
              <div class="link">Подробнее <img src='img/icons/arrow.png' /></div>
            </div>
          </router-link>

        </div>

        <div class="block2-load-wrapp load-wrapp" v-else>
          <div class="load-3">
            <div class="line"></div>
            <div class="line"></div>
            <div class="line"></div>
          </div>
        </div>

      </div>
    </section>
    <section class="block3">
      <div class="container">
        <h2 class="section__title"> <span class="title">Предоставляем качественный сервис
						<div class="before"></div>
						<div class="after"> </div></span></h2>
        <div class="block3__flex1">
          <div class="block3__item">
            <div class="block3__img block3__img1"><img src="img/block3/1.png" alt=""/></div>
            <div class="title">Доставка</div>
            <div class="text">Осуществляем доставку <br>по Владивостоку </div>
          </div>
          <div class="block3__item block3__item1">
            <div class="block3__img block3__img2"><img src="img/block3/2.png" alt=""/></div>
            <div class="title">Индивидуальные заказы</div>
            <div class="text">Создаём индивидуальные заказы для <br>различных мероприятий и праздников</div>
          </div>
          <div class="block3__item">
            <div class="block3__img block3__img3"><img src="img/block3/3.png" alt=""/></div>
            <div class="title">Самовывоз</div>
            <div class="text">Вы можете забрать товар, в у нас <br>в салоне, в удобное для вас время</div>
          </div>
        </div>
        <div class="block3__flex2">
          <div class="block3__item">
            <div class="block3__img block3__img4"><img src="img/block3/4.png" alt=""/></div>
            <div class="title">Удобный способ оплаты</div>
            <div class="text">Принимаем все виды оплаты, банковские <br>карты и другие виды переводов</div>
          </div>
          <div class="block3__item">
            <div class="block3__img block3__img5"><img src="img/block3/5.png" alt=""/></div>
            <div class="title">Аренда товаров для праздника</div>
            <div class="text">Предоставляем аренду посуды, свечей, <br>игрушек и другого вида декора</div>
          </div>
        </div>
      </div>
    </section>
    <section class="block4">
      <div class="container">
        <h2 class="section__title"> <span class="title">Cделайте свой праздник незабываемым с <br><span>"Konfetti Balloon"</span>
						<div class="before"></div>
						<div class="after"></div></span></h2>
        <div class="block2__flex block4__flex">
          <router-link to="/decoration" class="block2__item block4__item">
            <div style="background-image: url(&quot;img/block4/1.png&quot;)" class="block2__item__img"></div>
            <div class="block2__item__text">
              <div class="title">Оформление праздников</div>
              <div class="text">Оформление детских праздников, корпортаративов, декорирование мероприятий</div>
              <div class="link">Подробнее <img src='img/icons/arrow.png' /></div>
            </div>
          </router-link>
          <router-link to="/baloons" class="block2__item block4__item">
            <div style="background-image: url(&quot;img/block4/2.png&quot;)" class="block2__item__img"></div>
            <div class="block2__item__text">
              <div class="title">Воздушные шары</div>
              <div class="text">Оформление детских праздников, корпортаративов, декорирование мероприятий</div>
              <div class="link">Подробнее <img src='img/icons/arrow.png' /></div>
            </div>
          </router-link>
          <router-link to="/celebration" class="block2__item block4__item">
            <div style="background-image: url(&quot;img/block4/3.png&quot;)" class="block2__item__img"></div>
            <div class="block2__item__text">
              <div class="title">Аренда товаров для праздников</div>
              <div class="text">Оформление детских праздников, корпортаративов, декорирование мероприятий</div>
              <div class="link">Подробнее <img src='img/icons/arrow.png' /></div>
            </div>
          </router-link>
          <router-link to="/top" class="block2__item block4__item">
            <div style="background-image: url(&quot;img/block4/4.png&quot;)" class="block2__item__img"></div>
            <div class="block2__item__text">
              <div class="title">Популярные товары</div>
              <div class="text">Оформление детских праздников, корпортаративов, декорирование мероприятий</div>
              <div class="link">Подробнее <img src='img/icons/arrow.png' /></div>
            </div>
          </router-link>
        </div>
      </div>
    </section>
    <section class="block5">
      <div class="container">
        <h2 class="section__title"> <span class="title">Посмотрите отзывы наших <br>довольных клиентов
						<div class="before"></div>
						<div class="after"> </div></span></h2>
        <carousel
                class="block5__slider"
                v-if="reviews.length != 0"
                :items=1
                :nav=true
                :navText="nav_text"
        >
          <div class="block5__slide" v-for="(review, i) in reviews" :key="i">
            <div :style="`background-image: url(http://127.0.0.1:8000/${review.image_thumb})`" class="block5__img"></div>
            <div class="name">{{review.name}}</div>
            <div class="text">{{review.text}}</div>
          </div>
        </carousel>

        <div class="block2-load-wrapp load-wrapp" v-else>
          <div class="load-3">
            <div class="line"></div>
            <div class="line"></div>
            <div class="line"></div>
          </div>
        </div>

      </div>
    </section>
    <section class="block6">
      <div class="container">
        <h2 class="section__title"> <span class="title">Наши идеи
						<div class="before"></div>
						<div class="after"> </div></span></h2>
        <div class="block6__descriptor">Мы всегда рады поделиться своими свежими идеями</div>

        <div class="block6__flex" v-if="ideas.length != 0">

          <a href="/"
             class="block6__item"
             v-for="idea in ideas"
             :key="idea.id"
             :data-title="idea.name"
             :data-text="idea.text"
             :data-image="`http://127.0.0.1:8000/${idea.image_thumb}`"
          >
            <div class="block2__item__text block6__item__text">
              <div class="title">{{idea.name}}</div>
              <div class="text">{{trimString(idea.text, 145)}}</div>
              <div class="link">Подробнее <img src='img/icons/arrow.png' /></div>
            </div>
          </a>

        </div>

        <div class="block2-load-wrapp load-wrapp" v-else>
          <div class="load-3">
            <div class="line"></div>
            <div class="line"></div>
            <div class="line"></div>
          </div>
        </div>

      </div>
    </section>
    <section class="block7">
      <div class="container">
        <h2 class="section__title"> <span class="title">Новинки
						<div class="before"></div>
						<div class="after"> </div></span></h2>

        <carousel
                class="block7__slider"
                v-if="products.length != 0"
                :responsiveClass="true"
                :margin="30"
                :addClassActive="true"
                :nav="true"
                :navText="nav_text"
                :responsive="block7_responsive"
        >

          <div class="block7__item" v-for="(product, i) in products" :key="i">
            <a :href="`http://127.0.0.1:8000/${product.image}`"
               :data-lightbox="`product${i}`"
               :style="`background-image: url(http://127.0.0.1:8000/${product.image_thumb})`"
               class="block7__img"></a>
            <div class="title">{{product.name}}</div>
            <div class="block7__bottom">
              <div class="price">{{product.price}} р.</div>
              <div class="link" :data-type="`Заказ ${product.name}`">Купить <img src='img/icons/arrow.png' /></div>
            </div>
          </div>

        </carousel>

        <div class="block2-load-wrapp load-wrapp" v-else>
          <div class="load-3">
            <div class="line"></div>
            <div class="line"></div>
            <div class="line"></div>
          </div>
        </div>

      </div>
    </section>
  </div>
</template>

<script>
    import $ from 'jquery'
    import carousel from 'vue-owl-carousel'
    import 'lightbox2/dist/css/lightbox.min.css'
    import 'lightbox2/dist/js/lightbox.min'

    export default {
        name: 'Home',
        components: {carousel},
        data: () => ({
            block2: [],
            reviews: [],
            ideas: [],
            products: [],
            nav_text: ["<img src='img/icons/prev.png'/>",
                "<img src='img/icons/next.png'/>"],
            block7_responsive: {
                0:{
                    items:1
                },
                750:{
                    items:2
                },
                1170:{
                    items:4
                }
            }
        }),
        created: function(){
            this.getBlock2()
            this.getReviews()
            this.getIdeas()
            this.getProducts()
        },
        methods: {
            getBlock2() {
                $.ajax({
                    url: 'http://127.0.0.1:8000/api/v1/categories/index/',
                    type: 'GET',
                    success: (data) => {
                        this.block2 = data
                    },
                    error: (err) => {
                        this.block2 = err
                    }
                })
            },
            getReviews(){
                $.ajax({
                    url: 'http://127.0.0.1:8000/api/v1/reviews/',
                    type: 'GET',
                    success: (data) => {
                        this.reviews = data
                    },
                    error: (err) => {
                        this.reviews = err
                    }
                })
            },
            getIdeas() {
                $.ajax({
                    url: 'http://127.0.0.1:8000/api/v1/ideas/?is_main=1',
                    type: 'GET',
                    success: (data) => {
                        this.ideas = data
                    },
                    error: (err) => {
                        this.ideas = err
                    }
                })
            },
            trimString(str, max_len) {
                if (str.length < max_len) return str
                let trimmedString = str.substr(0, max_len);
                return trimmedString.substr(0, Math.min(trimmedString.length, trimmedString.lastIndexOf(" "))) + '...'
            },
            getProducts(){
                $.ajax({
                    url: 'http://127.0.0.1:8000/api/v1/products/?is_main=1',
                    type: 'GET',
                    success: (data) => {
                        this.products = data
                    },
                    error: (err) => {
                        this.products = err
                    }
                })
            }
        }
    }
</script>

<style>
  .owl-theme .owl-nav [class*='owl-'] {
    margin: 0;
    padding: 0;
    background-color: transparent;
  }
  .owl-theme .owl-nav [class*='owl-']:hover {
    background-color: transparent;
  }
  .owl-theme .owl-dots .owl-dot.active span, .owl-theme .owl-dots .owl-dot:hover span, .owl-theme .owl-dots .owl-dot span {
    display: none;
  }
</style>