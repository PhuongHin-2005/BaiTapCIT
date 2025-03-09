// 1. Khai báo biến
var n = 5;
var a = 2, b = -4;
var x = 7;
var y = 16;

// 2. Kiểm tra số nguyên dương
function kiemTraSoNguyenDuong(n) {
    if (n > 0) {
        if (n % 1 === 0) {
            return true;
        }
    }
    return false;
}

// 3. Kiểm tra số nguyên âm
function kiemTraSoNguyenAm(n) {
    if (n < 0) {
        if (n % 1 === 0) {
            return true;
        }
    }
    return false;
}

// 4. Tính tổng hai số
function tinhTong(a, b) {
    return a + b;
}

// 5. Giải phương trình bậc 1 (ax + b = 0)
function giaiPhuongTrinhBacMot(a, b) {
    if (a === 0) 
    {
        if (b === 0) {
            return 'Phương trình có vô số nghiệm';
        } else {
            return 'Phương trình vô nghiệm';
        }
    }
    return -b / a;
}

// 6. Kiểm tra số nguyên tố
function kiemTraSoNguyenTo(n) {
    if (n < 2) {
        return false;
    }
    var i=2;
    while (i<n) {
        if (n % i === 0) {
            return false;
        }
        i++;
    }
    return true;

}

// 7. Kiểm tra số chính phương
function kiemTraSoChinhPhuong(n) {
    if (n < 0) {
        return false;
    }
    var i = 1;
    while (i * i <= n) {
        if (i * i === n) {
            return true;
        }
        i++;
    }
    return false;
}

// 8. Chạy hàm
console.log(kiemTraSoNguyenDuong(n)); 
console.log(kiemTraSoNguyenAm(-n)); 
console.log(tinhTong(a, b)); 
console.log(giaiPhuongTrinhBacMot(a, b));
console.log(kiemTraSoNguyenTo(x)); 
console.log(kiemTraSoChinhPhuong(y)); 
