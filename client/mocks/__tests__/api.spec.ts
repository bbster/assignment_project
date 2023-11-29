import { describe, it, expect } from 'vitest'
// import { mount } from '@vue/test-utils'

describe('Mock API', () => {
  it('/compaines', async () => {
    const response = await fetch('http://49.1.213.232:8000/api/v1/companies', { method: 'GET' })
    console.log(await response.json())
    // const wrapper = mount(HelloWorld, { props: { msg: 'Hello Vitest' } })
    // expect(wrapper.text()).toContain('Hello Vitest')
  })
})
