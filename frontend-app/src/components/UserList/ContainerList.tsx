import { useContainers } from "../../hooks/useContainers";

const ContainerList = () => {
  const { containers, loading, error } = useContainers();

  if (loading) return <p>Загрузка...</p>;
  if (error) return <p style={{ color: "red" }}>{error}</p>;

  return (
    <div>
      <h2>Список контейнеров</h2>
      <ul>
        {containers.map((container) => (
          <li key={container.container_id}>
            <strong>Тип:</strong> {container.type || "Не указан"} <br />
            <strong>Статус:</strong> {container.status} <br />
            <strong>Местоположение:</strong> {container.location || "Не указано"}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ContainerList;
