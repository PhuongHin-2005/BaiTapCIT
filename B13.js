// 1. Hàm (Function)

// Tính giai thừa của số n bằng đệ quy
function tinh_giai_thua(n) {
    if (n <= 1) return 1;
    return n * tinh_giai_thua(n - 1);
}

/**
 * Tính số Fibonacci thứ n với memoization
 * @param {number} n
 * @param {object} bo_nho
 * @returns {number}
 */
function tinh_fibonacci(n, bo_nho = {}) {
    if (n in bo_nho) return bo_nho[n];
    if (n <= 1) return n;
    bo_nho[n] = tinh_fibonacci(n - 1, bo_nho) + tinh_fibonacci(n - 2, bo_nho);
    return bo_nho[n];
}

// 2. Chuỗi (String)

/**
 * Kiểm tra chuỗi đối xứng (palindrome)
 * @param {string} chuoi
 * @returns {boolean}
 */
function kiem_tra_doi_xung(chuoi) {
    return chuoi === chuoi.split('').reverse().join('');
}

/**
 * Tìm ký tự xuất hiện nhiều nhất trong chuỗi
 * @param {string} chuoi
 * @returns {string}
 */
function tim_ky_tu_pho_bien(chuoi) {
    let tan_suat = {};
    let ky_tu_nhieu_nhat = '';
    let so_lan_xuat_hien_max = 0;
    
    for (let ky_tu of chuoi) {
        tan_suat[ky_tu] = (tan_suat[ky_tu] || 0) + 1;
        if (tan_suat[ky_tu] > so_lan_xuat_hien_max) {
            so_lan_xuat_hien_max = tan_suat[ky_tu];
            ky_tu_nhieu_nhat = ky_tu;
        }
    }
    return ky_tu_nhieu_nhat;
}

// 3. Đối tượng và Lớp

class Nhan_vat {
    constructor(ten, tuoi) {
        this.ten = ten;
        this.tuoi = tuoi;
    }
}

class Hinh_chu_nhat {
    constructor(rong, dai) {
        this.rong = rong;
        this.dai = dai;
    }
    tinh_dien_tich() {
        return this.rong * this.dai;
    }
    tinh_chu_vi() {
        return 2 * (this.rong + this.dai);
    }
}

// 4. Vòng lặp (Loop)

/**
 * Kiểm tra số nguyên tố
 * @param {number} x
 * @returns {boolean}
 */
function kiem_tra_so_nguyen_to(x) {
    if (x < 2) return false;
    for (let i = 2; i <= Math.sqrt(x); i++) {
        if (x % i === 0) return false;
    }
    return true;
}

/**
 * In ra tất cả số nguyên tố từ 1 đến n
 * @param {number} n
 * @returns {number[]}
 */
function liet_ke_so_nguyen_to(n) {
    return Array.from({ length: n }, (_, i) => i + 1).filter(kiem_tra_so_nguyen_to);
}

/**
 * Tính tổng các số chia hết cho 3 hoặc 5 từ 1 đến n
 * @param {number} n
 * @returns {number}
 */
function tong_so_chia_het_cho_3_hoac_5(n) {
    return Array.from({ length: n }, (_, i) => i + 1).filter(x => x % 3 === 0 || x % 5 === 0).reduce((a, b) => a + b, 0);
}

// 5. Xử lý mảng (Array)

/**
 * Tìm số lớn thứ hai trong mảng (không dùng sort)
 * @param {number[]} mang
 * @returns {number|null}
 */
function tim_so_lon_thu_hai(mang) {
    let [lon_nhat, lon_thu_hai] = [-Infinity, -Infinity];
    for (let so of mang) {
        if (so > lon_nhat) {
            [lon_thu_hai, lon_nhat] = [lon_nhat, so];
        } else if (so > lon_thu_hai && so < lon_nhat) {
            lon_thu_hai = so;
        }
    }
    return lon_thu_hai === -Infinity ? null : lon_thu_hai;
}

/**
 * Đếm số lần xuất hiện của mỗi phần tử trong mảng
 * @param {number[]} mang
 * @returns {object}
 */
function dem_so_lan_xuat_hien(mang) {
    return mang.reduce((tan_suat, so) => {
        tan_suat[so] = (tan_suat[so] || 0) + 1;
        return tan_suat;
    }, {});
}

// Gọi các hàm và hiển thị kết quả

console.log("Giai thừa của 10:", tinh_giai_thua(10));
console.log("Số Fibonacci thứ 10:", tinh_fibonacci(10));
console.log("Chuỗi 'Hello' có đối xứng không?", kiem_tra_doi_xung("Hello"));
console.log("Ký tự xuất hiện nhiều nhất trong 'Nguyễn Thị Phương Hiền':", tim_ky_tu_pho_bien("Nguyễn Thị Phương Hiền"));

let nhan_vat = new Nhan_vat("Hien", 20);
console.log("Nhân vật:", nhan_vat);

let hinh = new Hinh_chu_nhat(2, 5);
console.log("Diện tích hình chữ nhật:", hinh.tinh_dien_tich());
console.log("Chu vi hình chữ nhật:", hinh.tinh_chu_vi());

console.log("Các số nguyên tố từ 1 đến 20:", liet_ke_so_nguyen_to(20));
console.log("Tổng các số chia hết cho 3 hoặc 5 từ 1 đến 10:", tong_so_chia_het_cho_3_hoac_5(10));

let mang_so = [1, 2, 3, 4, 5, 9, 7, 7, 8, 6, 5];
console.log("Số lớn thứ hai trong mảng:", tim_so_lon_thu_hai(mang_so));
console.log("Số lần xuất hiện của mỗi phần tử trong mảng:", dem_so_lan_xuat_hien(mang_so));
