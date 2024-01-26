export default function guardrail(mathFunction) {
  const queue = [];
  try {
    const func = mathFunction();
    queue.push(func);
  } catch (error) {
    queue.push(`${error}`);
  } finally {
    queue.push('Guardrail was processed');
  }

  return queue;
}
