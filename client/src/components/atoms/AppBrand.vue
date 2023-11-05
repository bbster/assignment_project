<script setup lang="ts">
const router = useRouter()

const routes = router.getRoutes()

const routeMap = computed(() => Object.fromEntries(routes.map((r) => [r.name, r])))
</script>

<template>
  <span class="app-brand">
    <RouterLink :to="routeMap['home']">홈</RouterLink>
  </span>
</template>

<style lang="scss" scoped>
.app-brand {
  padding: 8px 12px;
  text-align: center;
  a {
    font-size: 1em;
    font-weight: 600;
    color: #444444;
  }
}
</style>
