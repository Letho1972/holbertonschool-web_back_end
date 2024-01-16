export default function createReportObject(employeesList) {
  const allEmployees = { ...employeesList };

  const getNumberOfDepartments = function (employees) {
    return Object.keys(employees).length;
  };

  return {
    allEmployees,
    getNumberOfDepartments,
  };
}
