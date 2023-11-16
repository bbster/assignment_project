const BASE_API_URL = 'http://49.1.213.232:8000/api/v1'

export const useSignin = () => {
  const execute = async (account: Account) => {
    const requestOptions = {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(account)
    }

    const response = await fetch(`${BASE_API_URL}/account/login`, requestOptions)
    const data = (await response.json()) as APIRouterReturnType<`/account/login`, 'post'>

    return data
  }

  return { execute }
}
