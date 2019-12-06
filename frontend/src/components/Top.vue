<template>
    <div>
        <section class="block9"><img src="img/top/bg.png" alt="" class="block__bg block9__bg"/>
            <div class="container">
                <h1>Популярные <br>темы</h1>
                <button class="button block9__button" @click="slide_down('.block10')">Выбрать шары</button>
            </div>
        </section>
        <section class="block10">
            <div class="container">
                <div class="block10__container">
                    <aside class="block10__menu">
                        <select class="block10__menu-mobile">
                            <optgroup :label="cat.name" v-for="(cat, i) in categories" :key="i">
                                <option v-for="(subcat, j) in cat.children" :key="j" :data-id="subcat.id">{{subcat.name}}</option>
                            </optgroup>
                        </select>

                        <div v-bind:class="{'block10__menu__item-active': is_menu_item_active(cat)}"
                             class="block10__menu__item"
                             v-for="(cat, i) in categories"
                             :key="i"
                        >
                            <div class="block10__menu__head" @click="menu_toggle($event)">{{cat.name}}</div>
                            <div class="block10__menu__body">
                                <div class="block10__menu__link"
                                     @click="getProducts(subcat.id)"
                                     v-for="(subcat, j) in cat.children" :key="j"
                                >{{subcat.name}}</div>
                            </div>
                        </div>
                    </aside>
                    <div class="block10__main">
                        <div v-if="products.data.length != 0 && products.errors != 1">
                            <div class="block10__flex">

                                <div class="block7__item" v-for="(product, i) in products.data" :key="i">
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
                            </div>
                            <div
                                class="block10__load"
                                @click="getProducts(current_cat, products.next_page, load_next_page=true)"
                                v-if="products.next_page != 'end'"
                            >Загрузить ещё</div>
                        </div>
                        <div class="block10-load-wrapp load-wrapp" v-else-if="products.data.length == 0 && products.errors != 1">
                            <div class="load-3">
                                <div class="line"></div>
                                <div class="line"></div>
                                <div class="line"></div>
                            </div>
                        </div>
                        <div class="products-empty" v-else>В выбранной категории нет товаров.</div>
                    </div>
                </div>
            </div>
        </section>
        <section class="block11">
            <div class="container">
                <div class="block11__flex">
                    <div class="block11__left">
                        <div class="title">Планируете украсить <br>праздник или <br>мероприятие?</div>
                        <div class="text">Позвоните нам и наши декораторы посоветуют вам отличные идеи и помогут красиво оформить ваш праздник</div><img src="img/baloons/1.png" alt=""/>
                    </div>
                    <form class="block11__right form-type1">
                        <div class="title">Заказать звонок</div>
                        <div class="descriptor">Наш декоратор свяжется с вами <br>в течение 5 минут</div>
                        <input type="text" name="name" placeholder="Введите имя"/>
                        <input type="text" name="phone" placeholder="Введите телефон" required="required"/>
                        <textarea name="text" placeholder="Укажите ваши пожелания"></textarea>
                        <input type="hidden" name="type" value="Заявка на обратный звонок">
                        <button class="button">Выбрать шары</button>
                        <div class="checkbox">
                            <input type="checkbox" id="c1" checked="checked"/>
                            <label for="c1">
                                <div class="box"><img src="img/icons/check.png" alt=""/></div>
                                <div class="text">Я принимаю условия политики конфиденциальности и даю сагласие на обработку персональных данных</div>
                            </label>
                        </div>
                    </form>
                </div>
            </div>
        </section>
        <section class="block12">
			<div class="container">
				<div class="block12__flex">
					<div class="title">Популярные <br>темы</div>
					<div class="text">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla quam velit, vulputate eu pharetra nec, mattis ac neque. Duis vulputate commodo lectus, ac blandit elit tincidunt id. Sed rhoncus, tortor sed eleifend tristique, tortor mauris molestie elit, et lacinia ipsum quam nec dui. <br><br> Quisque nec mauris sit amet elit iaculis pretium sit amet quis magna. Aenean velit odio, elementum in tempus ut, vehicula eu diam. Pellentesque rhoncus aliquam mattis. Ut vulputate eros sed felis sodales nec vulputate justo hendrerit. Vivamus varius pretium ligula, a aliquam odio euismod sit amet. Quisque laoreet sem sit amet orci ullamcorper at ultricies metus viverra. Pellentesque arcu mauris, malesuada quis ornare accumsan, blandit sed diam.</div>
				</div>
			</div>
		</section>
    </div>
</template>

<script>
    import $ from 'jquery'
    import 'lightbox2/dist/css/lightbox.min.css'
    import 'lightbox2/dist/js/lightbox.min'

    export default {
        name: "Top",
        data: () => ({
            categories: [],
            current_cat: 0,
            products: {
                data: [],
                errors: ''
            }
        }),
        created: function(){
            this.current_cat = this.$route.query.category != undefined ? this.$route.query.category : 0
            this.getCategories()
        },
        methods: {
            menu_toggle(){
                $(event.target).parent().toggleClass('block10__menu__item-active')
            },
            slide_down(select) {
                var destination = $(select).offset().top;
                $('html, body').animate({ scrollTop: destination}, 500);
                return false;
            },
            getCategories(){
                $.ajax({
                    url: 'http://127.0.0.1:8000/api/v1/categories/',
                    type: 'GET',
                    success: (data) => {
                        this.categories = data
                        if (this.current_cat == 0) this.current_cat = this.categories[0].children[0].id
                        this.getProducts(this.current_cat)
                    },
                    error: (err) => {
                        this.categories = err
                    }
                })
            },
            getProducts(id, page=1, load_next_page=false){
                if (!load_next_page) this.products = {data: [], errors: ''}
                $.ajax({
                    url: `http://127.0.0.1:8000/api/v1/products/?is_top=1&category=${id}&is_paginated=1&page=${page}`,
                    type: 'GET',
                    success: (data) => {
                        if (load_next_page) {
                            this.products.data = this.products.data.concat(data.data)
                            this.products.next_page = data.next_page
                        } else {
                            if (data.data.length == 0) {
                                this.products.errors = 1;
                            } else {
                                this.products = data
                            }
                        }
                        this.current_cat = id
                    },
                    error: (err) => {
                        this.products = err
                    }
                })
            },
            is_menu_item_active(item){
                let id = this.current_cat

                for(let i = 0; i<item.children.length; i++) {
                    if (item.children[i].id == id) return true
                }
                if (item.id == id) return true
                else return false
            }
        }
    }

</script>

<style scoped>

</style>