const BASE_API_URL = 'http://49.1.213.232:8000/api/v1'

export const useFetchCompanies = () => {
  // const fetcher = createFetch({
  //   baseUrl: BASE_API_URL,
  //   fetchOptions: {},
  //   options: { fetch }
  // })

  const response = useFetch(`${BASE_API_URL}/companies`)
    .get()
    .json<APIRouterReturnType<`/companies`, 'get'>>()

  return response
}
