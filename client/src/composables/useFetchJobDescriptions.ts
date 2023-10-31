const BASE_API_URL =
  process.env.NODE_ENV === 'production' ? 'localhost' : 'http://49.1.213.232:8000/api/v1'

export const useFetchJobDescriptions = () => {
  // const fetcher = createFetch({
  //   baseUrl: BASE_API_URL,
  //   fetchOptions: {},
  //   options: { fetch }
  // })

  const response = useFetch(`${BASE_API_URL}/job-descriptions`)
    .get()
    .json<APIRouterReturnType<`/job-descriptions`, 'get'>>()

  return response
}
