import { z } from 'zod'
import * as Schema from './schema'

declare global {
  export type Company = z.infer<typeof Schema.company>

  export type APIRouters = {
    '/companies': {
      get: () => Company[]
    }
  }

  type APIRouterUrls = keyof APIRouters
  type AvailableRouterMethods<U extends APIRouterUrls> = APIRouters[U] extends undefined
    ? 'get'
    : keyof APIRouters[U]

  export type APIRouterReturnType<
    U extends APIRouterUrls,
    M extends AvailableRouterMethods<U>
  > = ReturnType<APIRouters[U][M]> extends undefined ? unknown : ReturnType<APIRouters[U][M]>
}
