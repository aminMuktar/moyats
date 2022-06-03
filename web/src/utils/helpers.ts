
export const parseDate = (timestamp: string) => {
  return new Date(timestamp).toLocaleString()
}

export const formAddress = (addr: any) => {
  return `${addr.city}, ${addr.country}`
}