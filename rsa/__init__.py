＃-*-编码：utf-8-*-
＃
＃版权所有2011 SybrenA.Stüvel<sybren@stuvel.eu>
＃
＃根据Apache许可证2.0版（“许可证”）获得许可；
＃除非符合许可，否则您不得使用此文件。
＃您可以在以下位置获得许可的副本
＃
＃https://www.apache.org/licenses/LICENSE-2.0
＃
＃除非适用法律要求或书面同意，否则软件
根据许可协议分发的＃是按“原样”分发的，
＃没有任何明示或暗示的保证或条件。
＃有关特定语言的管理权限，请参阅许可证。
＃许可中的限制。
“”“ RSA模块
用于计算大素数以及RSA加密，解密，签名的模块
和验证。包括生成公钥和私钥。
警告：此实现不使用将明文输入压缩为
防止重复或其他常见的安全性改进。小心使用。
“”

来自 rsa。密钥 导入 newkeys，PrivateKey，PublicKey
来自 rsa。pkcs1 导入 加密，解密，签名，验证，DecryptionError，
    VerificationError，find_signature_hash，   sign_hash，compute_hash

__author__  =  “ Sybren Stuvel，Barry Mead和Yesudeep Mangalapilly”
__date__  =  “ 2018-09-16”
__version__  =  '4.0'

＃如果我们直接运行就进行doctest
如果 __name__  ==  “ __main__”：
    导入 doctest

    doctest。testmod（）

__all__  = [[ “ newkeys”，“ encrypt”，“ decrypt”，“ sign”，“ verify”，“ PublicKey”，
           'PrivateKey'，'DecryptionError'，'VerificationError'，
           'compute_hash'，'sign_hash' ]
