<script setup lang="ts">
const router = useRouter()

const routes = router.getRoutes()

const routeMap = computed(() => Object.fromEntries(routes.map((r) => [r.name, r])))
</script>

<template>
  <nav class="app-navigation">
    <ul class="app-navigation__links">
      <li class="app-navigation__links__item">
        <RouterLink :to="routeMap['job-description']">채용</RouterLink>
      </li>
      <li class="app-navigation__links__item">
        <SigninDialogTrigger>대충 로그인</SigninDialogTrigger>
      </li>
    </ul>
  </nav>
</template>

<style lang="scss" scoped>
.app-navigation {
  &__links {
    display: flex;
    &__item {
      min-width: 120px;
      padding: 8px 12px;
      text-align: center;
      a {
        font-size: 1em;
        font-weight: 600;
        color: #444444;
      }
    }
  }
}
</style>
