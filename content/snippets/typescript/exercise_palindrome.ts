const s = "A man, a plan, a canal: Panama";
const cleaned = s.replace(/[^a-zA-Z0-9]/g, "").toLowerCase();
const isPalin = cleaned === cleaned.split("").reverse().join("");
console.log(isPalin ? "Palindrome" : "Not a palindrome");
function isPalindrome(s: string): boolean {
  const cleaned = s.toLowerCase().replace(/[^a-z0-9]/g, "");
  return cleaned === cleaned.split("").reverse().join("");
}

console.log(isPalindrome("A man, a plan, a canal: Panama"));
