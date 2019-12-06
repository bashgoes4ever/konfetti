<template>
    <div>
        <section class="block8">
            <div class="container">
                <div class="block8__block">
                    <div class="title">Контакты</div>
                    <div class="block8__item">
                        <div class="block8__icon"><img src="img/icons/5.png" alt=""/></div>
                        <span>{{contacts.phone1}}, {{contacts.phone2}}</span>
                    </div>
                    <div class="block8__item">
                        <div class="block8__icon"><img src="img/icons/6.png" alt=""/></div>
                        <span>{{contacts.email}}</span>
                    </div>
                    <div class="block8__item">
                        <div class="block8__icon"><img src="img/icons/7.png" alt=""/></div>
                        <span> г. {{contacts.city}}, <br>{{contacts.street}}</span>
                    </div>
                    <div class="block8__item">
                        <div class="block8__icon"><img src="img/icons/8.png" alt=""/></div>
                        <span>Часы работы <br>{{contacts.working_hours}}</span>
                    </div>
                    <div v-if="contacts.vk || contacts.instagram || contacts.facebook">
                        <div class="title2">Мы в социальных сетях</div>
                        <div class="block8__socials">
                            <a v-if="contacts.vk" :href="contacts.vk" target="_blank" class="block8__social"><img src="img/icons/9.png" alt=""/></a>
                            <a v-if="contacts.instagram" :href="contacts.instagram" target="_blank" class="block8__social"><img src="img/icons/10.png" alt=""/></a>
                            <a v-if="contacts.facebook" :href="contacts.facebook" target="_blank" class="block8__social"><img src="img/icons/11.png" alt=""/></a>
                        </div>
                    </div>
                </div>
            </div>
            <div id="map" v-html="contacts.map"></div>
        </section>
        <footer>
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
        </footer>
    </div>
</template>

<script>
    export default {
        name: "Footer",
        props: ['contacts']
    }
</script>