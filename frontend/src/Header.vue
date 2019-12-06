<template>
    <div>
        <header>
            <div class="container">
                <div class="header__flex"><router-link to="/" class="header__logo"><img src="img/logo.png" alt=""/>
                    <div class="text">Шары и аксессуары <br>для Ваших праздников</div></router-link>
                    <div class="header__right">
                        <div class="header__socials" v-if="contacts.whatsapp || contacts.viber || contacts.telegram">
                            <div class="title">Быстрая связь с нами</div>
                            <div class="header__socials__icons">
                                <a v-if='contacts.whatsapp' :href="contacts.whatsapp" target="_blank" class="header__social"><img src="img/icons/1.png" alt=""/></a>
                                <a v-if='contacts.viber' :href="contacts.viber" target="_blank" class="header__social"><img src="img/icons/2.png" alt=""/></a>
                                <a v-if='contacts.telegram' :href="contacts.telegram" target="_blank" class="header__social"><img src="img/icons/3.png" alt=""/></a>
                            </div>
                        </div>
                        <a :href="'http://127.0.0.1:8000/'+contacts.price_list" target="_blank">
                            <button class="button">Скачать прайс</button>
                        </a>
                        <div class="header__callback">
                            <div class="phone"><img src='img/icons/4.png' /> <span>{{contacts.phone1}}</span></div>
                            <div class="phone__callback" data-type="Заявка на обратный звонок">Заказать звонок</div>
                        </div>
                    </div>
                </div>
            </div>
        </header>
        <nav>
            <div class="container">
                <div class="nav__button">
                    <div class="box">
                        <div class="line line1"></div>
                        <div class="line line2"></div>
                        <div class="line line3"></div>
                    </div><span>Меню</span>
                </div>
                <div class="nav__flex"><img src="img/close.png" alt="" class="close-nav"/>
                    <router-link to="/baloons">Воздушные шары</router-link>
                    <router-link to="/decoration">Оформление праздников</router-link>
                    <router-link to="/celebration">Товары для праздника</router-link>
                    <router-link to="/sales">Акции</router-link>
                    <router-link to="/ideas">Идеи</router-link>
                    <a href="/" class="contacts-btn">Контакты</a>
                </div>
            </div>
        </nav>
    </div>
</template>

<script>
    export default {
        name: "Header",
        props: ['contacts']
    }
</script>