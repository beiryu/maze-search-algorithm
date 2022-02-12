# The algorithm for the maze

## Yêu cầu chi tiết

Cho một bản đồ mê cung như hình vẽ dưới, trong đó:

- Ký hiệu ngôi sao đại diện cho vị trí xuất phát của tác nhân.
- Ký hiệu x thể hiện các bức tường và tác nhân sẽ không thể di chuyển lên các vị trí này.
- Ký hiệu + thể hiện các ô điểm thưởng mà nếu tác nhân di chuyển vào các ô này sẽ được giảm chi phí thực hiện đường đi.

![alt text](https://github.com/beiryu/maze-search-algorithm/blob/main/map-view.png?raw=true)

- Ký hiệu exit đại diện cho vị trí đích mà tác nhân cần di chuyển đến, là vị trí duy nhất mà tác nhân có thể thoát khỏi mê cung. 

Mục tiêu là cài đặt các thuật toán tìm kiếm đường đi từ vị trí xuất phát đến vị trí đích (vị trí thoát khỏi mê cung) cho tác nhân. Trong đó tác nhân chỉ có thể di chuyển lên, xuống, trái, phải với chi phí bằng nhau. Các thuật toán được cài đặt:
- Thuật toán tìm kiếm không có thông tin: 
  - Thuật toán tìm kiếm DFS (Depth First Search).
  - Thuật toán tìm kiếm BFS (Breadth First Search).
- Thuật toán tìm kiếm có thông tin:
  - Thuật toán tìm kiếm tham lam (Greedy Best First Search).
  - Thuật toán tìm kiếm A*.

## Bản đồ trò chơi

Mỗi kịch bản kiểm thử được thiết kế như sau:

- Dòng đầu là số lượng điểm thưởng n (n = 0 với bản đồ không có điểm thưởng).
- n dòng tiếp theo, mỗi dòng sẽ bao gồm 3 số nguyên x,y, z với x,y là tọa độ của điểm thưởng trong ma trận; z là giá trị của điểm thưởng, sẽ là các số nguyên âm.
- Các dòng tiếp theo mô tả bản đồ của trò chơi. Các bạn lưu ý điểm kết thúc của hành trình sẽ là điểm thoát khỏi mê cung (ví dụ trong hình 2 thì điểm kết thúc sẽ là điểm ở dòng 2 và cột 0); điểm bắt đầu của tác nhân được ký hiệu bằng ký tự S; các ký tự x sẽ là các bức tường; các ký tự + sẽ là các điểm thưởng.

## Cách chạy mỗi thuật toán:
- Đối với thuật toán có heuristic: **python3 [algorithm].py [map].txt [heuristic]**
- Đối với thuật toán không có heuristic: **python3 [algorithm].py [map].txt**
- Đối với bản đồ có điểm thưởng: **python3 [algorithm].py [map].txt**
