import { createFetch } from '@vueuse/core'

const BASE_API_URL =
  process.env.NODE_ENV === 'production' ? 'http://localhost' : 'http://49.1.213.232:8000/api/v1'

export const useFetchCompanies = () => {
  console.log(process.env.NODE_ENV)
  const fetcher = createFetch({
    baseUrl: BASE_API_URL,
    fetchOptions: {},
    options: { fetch }
  })

  const response = fetcher('/companies', {}).get().json<APIRouterReturnType<'/companies', 'get'>>()
  return response
}
