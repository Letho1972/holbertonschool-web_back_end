export default function getStudentsByLocation(studentlist, city) {
  return studentlist.filter((key) => key.location === city);
}
