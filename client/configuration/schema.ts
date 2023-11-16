import { z } from 'zod'

const id = z.number()

export const company = z.object({
  id,
  company_name: z.string().max(100),
  country: z.string(),
  city: z.string()
})

export const jobDescription = z.object({
  id,
  company,
  position: z.string(),
  content: z.string(),
  reward: z.number(),
  skill: z.string().regex(/^([^,]*,){0,4}[^,]*$/),
  start_date: z.string(),
  end_date: z.string()
})

export const account = z.object({
  username: z.string(),
  password: z.string()
})
