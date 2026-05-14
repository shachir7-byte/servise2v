<template>
  <div id="app">
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
      <div class="container">
        <a class="navbar-brand fw-bold" href="#" @click.prevent="currentTab = 'orders'">
          <i class="fas fa-tools me-2"></i>Сервисный центр
        </a>
        <div class="collapse navbar-collapse">
          <ul class="navbar-nav ms-auto">
            <li class="nav-item">
              <a class="nav-link" :class="{ active: currentTab === 'orders' }" @click="currentTab = 'orders'">
                <i class="fas fa-list me-1"></i> Заказы
              </a>
            </li>
            <li class="nav-item">
              <a class="nav-link" :class="{ active: currentTab === 'clients' }" @click="currentTab = 'clients'">
                <i class="fas fa-users me-1"></i> Клиенты
              </a>
            </li>
            <li class="nav-item">
              <a class="nav-link" :class="{ active: currentTab === 'services' }" @click="currentTab = 'services'">
                <i class="fas fa-wrench me-1"></i> Услуги
              </a>
            </li>
          </ul>
        </div>
      </div>
    </nav>

    <div class="content-wrapper container mt-4">
      <div v-if="currentTab === 'clients'">
        <div class="position-relative mb-4 hero-banner">
          <img src="/clients.jpg" class="w-100 h-100 object-fit-cover" alt="Клиенты">
          <div class="position-absolute bottom-0 start-0 text-white p-3 bg-dark bg-opacity-25 w-100">
            <h1 class="mb-0 text-white">Клиенты</h1>
          </div>
        </div>
        
        <div class="row">
          <div v-for="client in db.clients" :key="client.id" class="col-md-6 col-lg-4 mb-3">
            <div class="card h-100 border-0 shadow-sm text-center p-3">
              <div class="bg-secondary rounded-circle mx-auto mb-3 d-flex align-items-center justify-content-center" style="width: 80px; height: 80px;">
                <i class="fas fa-user text-white fs-4"></i>
              </div>
              <h5 class="card-title text-dark">{{ client.last_name }} {{ client.first_name }}</h5>
              <p class="text-muted">{{ client.phone_number }}</p>
            </div>
          </div>
        </div>
      </div>

      <div v-if="currentTab === 'services'">
        <div class="position-relative mb-4 hero-banner">
          <img src="/services.jpg" class="w-100 h-100 object-fit-cover" alt="Услуги">
          <div class="position-absolute bottom-0 start-0 text-white p-3 bg-dark bg-opacity-25 w-100">
            <h1 class="mb-0 text-white">Наши услуги</h1>
          </div>
        </div>

        <div class="row">
          <div v-for="s in db.services" :key="s.id" class="col-md-4 mb-4">
            <div class="card h-100 text-center border-0 shadow-sm p-4">
              <div class="bg-primary rounded-circle mx-auto mb-3 d-flex align-items-center justify-content-center" style="width: 80px; height: 80px;">
                <i v-if="s.service_name.includes('стекла')" class="fas fa-shield-alt text-white fs-3"></i>
                <i v-else-if="s.service_name.includes('кодека')" class="fas fa-headphones text-white fs-3"></i>
                <i v-else class="fas fa-wrench text-white fs-3"></i>
              </div>
              <h5 class="card-title text-dark">{{ s.service_name }}</h5>
              <p class="card-text fs-4 fw-bold text-dark">{{ s.service_cost }} ₽</p>
            </div>
          </div>
        </div>
      </div>
      
      <div v-if="currentTab === 'orders'" class="text-center py-5">
        <h2>Список заказов</h2>
        <p class="text-muted">Здесь будет список активных ремонтов.</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import dbData from './db.json'

const currentTab = ref('orders')
const db = ref(dbData)
</script>

<style>
body { background-color: #f8f9fa; padding-top: 60px; }
.navbar { position: fixed; top: 0; width: 100%; z-index: 1000; }
.hero-banner { height: 200px; overflow: hidden; border-radius: 8px; }
.object-fit-cover { object-fit: cover; }
.card { transition: transform 0.2s; background: white; }
.card:hover { transform: translateY(-5px); }
</style>