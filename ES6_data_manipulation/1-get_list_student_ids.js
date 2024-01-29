export default function getListStudentIds(getListStudents) {
  if (!Array.isArray(getListStudents)) {
    return [];
  }
  const idArray = getListStudents.map((student) => student.id);

  return idArray;
}
