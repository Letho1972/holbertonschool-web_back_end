import ClassRoom from './0-classroom';
// Implement the initializeRooms function
export default function initializeRooms() {
  // Create an array of 3 ClassRoom objects with sizes 19, 20, and 34
  const array = [
    new ClassRoom(19),
    new ClassRoom(20),
    new ClassRoom(34),
  ];

  return array;
}
