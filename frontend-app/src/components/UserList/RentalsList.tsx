import dayjs from 'dayjs';
import { useRentals } from '../../hooks/useRentals';

const RentalList = () => {
    const {rentals, loading, error} = useRentals();
    
    if(loading) return <p>Загрузка...</p>
    if(error) return <p>Ошибка...</p>

    return (
        <div>
<h2>Список Аренд</h2>
<ul>
    {rentals.map((rental) => (
        <li key={rental}></li>
    ))}
</ul>
        </div>

    )
}
export default RentalList;