import {fetchRentals} from "../api"
import {useState, useEffect} from "react"
import {Rental} from '../types'

const useRentals = () => {
const [rentals, setRental] = useState<Rental[]>([])
const [loading, setLoading] = useState<boolean>(true)
const [error, setError] = useState<string | null>(null) 

useEffect(() => {
    const loadRentals = async () => {
        try {
            const data = await fetchRentals()
            setRental(data)
        } catch (error) {
            setError("Ошибка при запуске аренды")
        }finally{
            setLoading(false)
        }
    }
    loadRentals()
},[])

    return {rentals, loading, error}
}

export default useRentals;