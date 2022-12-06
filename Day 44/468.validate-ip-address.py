#
# @lc app=leetcode id=468 lang=python3
#
# [468] Validate IP Address
#

# @lc code=start
class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if '.' in queryIP:
            return self.validIPv4(queryIP)
        elif ':' in queryIP:
            return self.validIPv6(queryIP)
        else:
            return 'Neither' 

    def validIPv4(self, queryIP: str) -> str:
        if queryIP.count('.') != 3:
            return 'Neither'
        for ip in queryIP.split('.'):
            if not ip.isdigit() or len(ip) > 1 and ip[0] == '0' or int(ip) > 255:
                return 'Neither'
        return 'IPv4'

    def validIPv6(self, queryIP: str) -> str:
        if queryIP.count(':') != 7:
            return 'Neither'
        for ip in queryIP.split(':'):
            if not 1 <= len(ip) <= 4 or not all(c in string.hexdigits for c in ip):
                return 'Neither'
        return 'IPv6'
# @lc code=end

