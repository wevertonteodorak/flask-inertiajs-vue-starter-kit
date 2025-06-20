<template>
  <AppLayout>
    <div class="py-16">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-12">
          <h1 class="text-4xl font-bold text-gray-900 mb-4">
            {{ message }}
          </h1>
          <p class="text-xl text-gray-600 max-w-2xl mx-auto">
            Experiência SPA moderna com navegação fluida, componentes reativos e arquitetura robusta.
          </p>
        </div>
        
        <!-- Features Grid -->
        <div class="grid md:grid-cols-3 gap-8 mb-16">
          <div class="card p-6 text-center hover:shadow-lg transition-shadow">
            <div class="w-12 h-12 bg-blue-100 rounded-lg flex items-center justify-center mx-auto mb-4">
              <svg class="w-6 h-6 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path>
              </svg>
            </div>
            <h3 class="text-lg font-semibold text-gray-900 mb-2">Performance</h3>
            <p class="text-gray-600">Carregamento rápido com navegação SPA</p>
          </div>
          
          <div class="card p-6 text-center hover:shadow-lg transition-shadow">
            <div class="w-12 h-12 bg-green-100 rounded-lg flex items-center justify-center mx-auto mb-4">
              <svg class="w-6 h-6 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path>
              </svg>
            </div>
            <h3 class="text-lg font-semibold text-gray-900 mb-2">Simplicidade</h3>
            <p class="text-gray-600">Sem necessidade de API REST separada</p>
          </div>
          
          <div class="card p-6 text-center hover:shadow-lg transition-shadow">
            <div class="w-12 h-12 bg-purple-100 rounded-lg flex items-center justify-center mx-auto mb-4">
              <svg class="w-6 h-6 text-purple-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"></path>
              </svg>
            </div>
            <h3 class="text-lg font-semibold text-gray-900 mb-2">Moderno</h3>
            <p class="text-gray-600">Stack atual com Vue 3 e Composition API</p>
          </div>
        </div>
        
        <!-- Recent Users -->
        <div class="card p-6">
          
          <div class="grid gap-4 md:grid-cols-2">
            <div 
              v-for="user in users" 
              :key="user.id" 
              class="p-4 border border-gray-200 rounded-lg hover:bg-gray-50 transition-colors cursor-pointer"
              @click="goToUser(user.id)"
            >
              <div class="flex items-center space-x-3">
                <div class="w-10 h-10 bg-primary-100 rounded-full flex items-center justify-center">
                  <span class="text-primary-600 font-medium">
                    {{ user.name.charAt(0).toUpperCase() }}
                  </span>
                </div>
                <div>
                  <h3 class="font-medium text-gray-900">{{ user.name }}</h3>
                  <p class="text-gray-500 text-sm">{{ user.email }}</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </AppLayout>
</template>

<script setup>
import AppLayout from '@/layouts/AppLayout.vue'
import { Link, router } from '@inertiajs/vue3'

defineProps({
  message: String,
  users: Array
})

const goToUser = (id) => {
  router.visit(`/users/${id}`)
}
</script>