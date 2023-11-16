<script setup lang="ts">
const isDialogOpen = ref(false)
whenever(isDialogOpen, () => reset())

const { execute: signinAction } = useSignin()
const { cloned: account, sync: reset } = useCloned({ username: '', password: '' }, { manual: true })

const submit = async () => {
  const data = await signinAction(unref(account))
  window.alert(data.message)
}
</script>

<template>
  <AlertDialogRoot v-model:open="isDialogOpen">
    <AlertDialogTrigger
      class="bg-white text-grass11 font-semibold hover:bg-white/90 shadow-sm inline-flex h-[35px] items-center justify-center rounded-[4px] px-[15px] leading-none outline-none focus:shadow-[0_0_0_2px] focus:shadow-black transition-all"
    >
      <slot></slot>
    </AlertDialogTrigger>
    <AlertDialogPortal>
      <AlertDialogOverlay
        class="bg-blackA9 data-[state=open]:animate-overlayShow fixed inset-0 z-30"
      />
      <AlertDialogContent
        class="z-[100] text-[15px] data-[state=open]:animate-contentShow fixed top-[50%] left-[50%] max-h-[85vh] w-[90vw] max-w-[500px] translate-x-[-50%] translate-y-[-50%] rounded-[6px] bg-white p-[25px] shadow-[hsl(206_22%_7%_/_35%)_0px_10px_38px_-10px,_hsl(206_22%_7%_/_20%)_0px_10px_20px_-15px] focus:outline-none"
      >
        <AlertDialogTitle class="text-mauve12 m-0 text-[17px] font-semibold">
          응 어서오시고
        </AlertDialogTitle>
        <AlertDialogDescription class="text-mauve11 mt-4 mb-5 text-[15px] leading-normal">
          어디보자
        </AlertDialogDescription>

        <form>
          <Label class="text-[15px] font-semibold leading-[35px] text-black" for="username">
            여긴 니이름이고
          </Label>
          <input
            id="username"
            class="bg-white shadow-blackA9 block h-[35px] w-full appearance-none items-center justify-center rounded-[4px] px-[10px] text-[15px] leading-none text-black shadow-[0_0_0_1px] outline-none focus:shadow-[0_0_0_2px_black] selection:color-white selection:bg-blackA9"
            type="text"
            v-model="account.username"
          />

          <Label class="text-[15px] font-semibold leading-[35px] text-black" for="password">
            이건 비밀번호고
          </Label>
          <input
            id="password"
            class="bg-white shadow-blackA9 block h-[35px] w-full appearance-none items-center justify-center rounded-[4px] px-[10px] text-[15px] leading-none text-black shadow-[0_0_0_1px] outline-none focus:shadow-[0_0_0_2px_black] selection:color-white selection:bg-blackA9"
            type="password"
            v-model="account.password"
          />
        </form>

        <div class="flex justify-end gap-[25px] mt-4">
          <AlertDialogCancel
            class="text-black bg-blackA4 hover:bg-blackA5 focus:shadow-blackA7 inline-flex h-[35px] items-center justify-center rounded-[4px] px-[15px] font-semibold leading-none outline-none focus:shadow-[0_0_0_2px]"
          >
            응 안해
          </AlertDialogCancel>
          <AlertDialogAction
            class="text-white bg-green10 hover:bg-green11 focus:shadow-green12 inline-flex h-[35px] w-[180px] items-center justify-center rounded-[4px] px-[15px] font-semibold leading-none outline-none focus:shadow-[0_0_0_2px]"
            @click="submit"
          >
            드가자
          </AlertDialogAction>
        </div>
      </AlertDialogContent>
    </AlertDialogPortal>
  </AlertDialogRoot>
</template>
