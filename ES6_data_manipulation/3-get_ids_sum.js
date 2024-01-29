export default function getStudentIdsSum(Studentlist) {
  const student = 0;
  return Studentlist.reduce((total, addId) => total + addId.id, student);
}
