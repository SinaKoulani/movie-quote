<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const quote = ref(null)
const isLoading = ref(false)
const errorMessage = ref('')
const copied = ref(false)

const API_URL = 'http://127.0.0.1:8000/v1/quote/'

const featuredQuotes = [
  {
    quote: 'I am the one who knocks!',
    show: 'Breaking Bad',
    role: 'Walter White',
  },
  {
    quote: 'Winter is coming.',
    show: 'Game of Thrones',
    role: 'Ned Stark',
  },
  {
    quote: 'Why so serious?',
    show: 'The Dark Knight',
    role: 'Joker',
  },
]

const getQuote = async () => {
  isLoading.value = true
  errorMessage.value = ''
  copied.value = false

  try {
    const response = await axios.get(API_URL)
    quote.value = response.data
  } catch (error) {
    console.error(error)
    errorMessage.value = 'ارتباط با بک‌اند برقرار نشد. مطمئن شو سرور Django روشن است.'
  } finally {
    isLoading.value = false
  }
}

const copyQuote = async () => {
  if (!quote.value?.quote) return

  try {
    await navigator.clipboard.writeText(quote.value.quote)
    copied.value = true

    setTimeout(() => {
      copied.value = false
    }, 1800)
  } catch (error) {
    console.error(error)
  }
}

onMounted(() => {
  getQuote()
})
</script>

<template>
  <main dir="rtl" class="min-h-screen overflow-hidden bg-slate-950 text-white">
    <div class="fixed inset-0 -z-10">
      <div class="absolute inset-0 bg-gradient-to-br from-slate-950 via-indigo-950 to-purple-950"></div>
      <div class="absolute right-[-120px] top-[-120px] h-80 w-80 rounded-full bg-purple-600/30 blur-3xl"></div>
      <div class="absolute bottom-[-120px] left-[-120px] h-96 w-96 rounded-full bg-blue-600/30 blur-3xl"></div>
    </div>

    <header class="w-full border-b border-white/10 bg-white/5 backdrop-blur-xl">
      <div class="mx-auto flex max-w-6xl items-center justify-between px-6 py-5">
        <div class="flex items-center gap-3">
          <div class="flex h-11 w-11 items-center justify-center rounded-2xl bg-gradient-to-br from-indigo-400 to-purple-500 shadow-lg">
            🎬
          </div>

          <div class="text-right">
            <h1 class="text-lg font-bold">Movie Quote</h1>
            <p class="text-xs text-slate-400">Vue 3 + Django API</p>
          </div>
        </div>

        <a
          href="http://127.0.0.1:8000/admin/"
          target="_blank"
          class="rounded-xl bg-white/10 px-4 py-2 text-sm transition hover:bg-indigo-500/30 hover:text-indigo-100"
        >
          Admin
        </a>
      </div>
    </header>

    <section class="mx-auto grid max-w-6xl gap-12 px-6 py-16 lg:grid-cols-2 lg:items-center">
      <div class="text-right">
        <div class="mb-6 inline-flex items-center gap-2 rounded-full border border-emerald-400/20 bg-emerald-400/10 px-4 py-2 text-sm text-emerald-300">
          <span class="h-2 w-2 rounded-full bg-emerald-400 animate-pulse"></span>
          دریافت داده از بک‌اند Django
        </div>

        <h2 class="mb-6 text-4xl font-black leading-tight sm:text-5xl">
          نمایش دیالوگ‌های فیلم و سریال با
          <span class="bg-gradient-to-r from-indigo-300 to-purple-300 bg-clip-text text-transparent">
            Vue.js
          </span>
        </h2>

        <p class="mb-8 text-lg leading-8 text-slate-300">
          این پروژه یک نمونه MVP است که داده را از API جنگو دریافت می‌کند و با رابط کاربری مدرن،
          برای توسعه به بخش‌هایی مثل جستجو، لیست آثار و صفحه جزئیات آماده است.
        </p>

        <div class="flex flex-col gap-4 sm:flex-row sm:justify-end">
          <a
            href="http://127.0.0.1:8000/v1/quote/"
            target="_blank"
            class="rounded-2xl bg-white/10 px-6 py-4 text-center font-bold transition hover:bg-white/20"
          >
            مشاهده API
          </a>

          <button
            @click="getQuote"
            class="rounded-2xl bg-indigo-500 px-6 py-4 font-bold shadow-lg shadow-indigo-500/30 transition hover:bg-indigo-600 active:scale-95"
          >
            دریافت دیالوگ جدید
          </button>
        </div>
      </div>

      <div class="relative">
        <div class="absolute -inset-1 rounded-[2rem] bg-gradient-to-r from-indigo-500 to-purple-500 opacity-40 blur"></div>

        <div class="relative rounded-[2rem] border border-white/20 bg-white/10 p-8 shadow-2xl backdrop-blur-xl sm:p-10">
          <div class="mb-8 flex items-center justify-between">
            <button
              @click="copyQuote"
              class="flex h-11 w-11 items-center justify-center rounded-2xl bg-white/10 transition hover:bg-white/20"
              title="کپی کردن"
            >
              📋
            </button>

            <div class="text-right">
              <p class="text-sm text-slate-400">دیالوگ منتخب</p>
              <h3 class="mt-1 text-2xl font-bold">Now Showing</h3>
            </div>
          </div>

          <div v-if="isLoading" class="py-20 text-center">
            <div class="mx-auto h-12 w-12 rounded-full border-4 border-white/20 border-t-indigo-400 animate-spin"></div>
            <p class="mt-5 text-slate-300">در حال دریافت دیتا از بک‌اند...</p>
          </div>

          <div v-else-if="errorMessage" class="py-16 text-center">
            <div class="mb-5 text-5xl">⚠️</div>
            <p class="leading-7 text-red-300">{{ errorMessage }}</p>
          </div>

          <div v-else-if="quote" class="text-right">
            <div class="mb-4 text-7xl font-serif text-indigo-300">“</div>

            <p class="mb-8 text-2xl font-bold leading-relaxed sm:text-3xl">
              {{ quote.quote }}
            </p>

            <div class="flex items-start justify-between gap-4 border-t border-white/10 pt-6">
              <div class="text-right">
                <p class="text-sm text-slate-400">شخصیت</p>
                <p class="mt-1 text-lg font-bold">{{ quote.role || 'نامشخص' }}</p>
              </div>

              <div class="text-right">
                <p class="text-sm text-slate-400">فیلم / سریال</p>
                <p class="mt-1 text-lg font-bold">{{ quote.show || 'نامشخص' }}</p>
              </div>
            </div>

            <p v-if="copied" class="mt-5 text-sm text-emerald-300">
              دیالوگ با موفقیت کپی شد.
            </p>
          </div>
        </div>
      </div>
    </section>

    <section class="mx-auto max-w-6xl px-6 pb-8">
      <div class="mb-6 text-right">
        <h3 class="text-2xl font-bold">چند دیالوگ معروف</h3>
        <p class="mt-2 text-slate-400">
          این بخش نمایشی است و برای ارائه بهتر چند نمونه شناخته‌شده را نشان می‌دهد.
        </p>
      </div>

      <div class="grid gap-5 md:grid-cols-3">
        <article
          v-for="item in featuredQuotes"
          :key="item.quote"
          class="group rounded-3xl border border-white/10 bg-white/5 p-6 transition duration-300 hover:-translate-y-1 hover:border-indigo-400/40 hover:bg-gradient-to-br hover:from-indigo-500/20 hover:to-purple-500/20"
        >
          <div class="mb-4 text-3xl transition group-hover:text-indigo-300">🎞️</div>
          <p class="mb-5 min-h-[96px] text-lg font-semibold leading-8 text-slate-100">
            {{ item.quote }}
          </p>
          <div class="border-t border-white/10 pt-4 text-right">
            <p class="text-sm text-slate-400">شخصیت</p>
            <p class="font-bold text-indigo-200">{{ item.role }}</p>
            <p class="mt-3 text-sm text-slate-400">فیلم / سریال</p>
            <p class="font-bold text-purple-200">{{ item.show }}</p>
          </div>
        </article>
      </div>
    </section>

    <section class="mx-auto max-w-6xl px-6 pb-16">
      <div class="grid gap-5 md:grid-cols-3">
        <div class="group rounded-3xl border border-white/10 bg-white/5 p-6 transition duration-300 hover:border-indigo-400/40 hover:bg-indigo-500/15">
          <div class="mb-4 text-3xl transition group-hover:text-indigo-300">⚡</div>
          <h4 class="mb-3 text-xl font-bold">فرانت‌اند سریع</h4>
          <p class="leading-7 text-slate-400">
            ساخته‌شده با Vue 3 و Vite برای تجربه سریع، سبک و قابل توسعه.
          </p>
        </div>

        <div class="group rounded-3xl border border-white/10 bg-white/5 p-6 transition duration-300 hover:border-purple-400/40 hover:bg-purple-500/15">
          <div class="mb-4 text-3xl transition group-hover:text-purple-300">🔌</div>
          <h4 class="mb-3 text-xl font-bold">اتصال به بک‌اند</h4>
          <p class="leading-7 text-slate-400">
            داده‌ها از endpoint واقعی جنگو خوانده می‌شوند و در رابط کاربری نمایش داده می‌شوند.
          </p>
        </div>

        <div class="group rounded-3xl border border-white/10 bg-white/5 p-6 transition duration-300 hover:border-pink-400/40 hover:bg-pink-500/15">
          <div class="mb-4 text-3xl transition group-hover:text-pink-300">🛠️</div>
          <h4 class="mb-3 text-xl font-bold">قابل توسعه</h4>
          <p class="leading-7 text-slate-400">
            امکان افزودن جستجو، دسته‌بندی، لیست آثار و صفحه جزئیات وجود دارد.
          </p>
        </div>
      </div>
    </section>

    <footer class="border-t border-white/10 bg-white/5">
      <div class="mx-auto flex max-w-6xl flex-col items-center justify-between gap-3 px-6 py-6 text-sm text-slate-400 sm:flex-row">
        <p class="transition hover:text-indigo-300">Movie Quote MVP</p>
        <p class="transition hover:text-purple-300">Django API: {{ API_URL }}</p>
      </div>
    </footer>
  </main>
</template>

<style scoped>
button,
a {
  cursor: pointer;
}
</style>
