export default function taskBlock(trueOrFalse) {
  const task = false;
  const task2 = true;

  if (trueOrFalse) {
    task = true;
    task2 = false;
  }
  
  let task = false;
  let task2 = true;

  return [task, task2];
}
