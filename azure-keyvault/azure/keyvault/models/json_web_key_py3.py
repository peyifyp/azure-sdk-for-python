# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class JsonWebKey(Model):
    """As of http://tools.ietf.org/html/draft-ietf-jose-json-web-key-18.

    :param kid: Key identifier.
    :type kid: str
    :param kty: JsonWebKey key type (kty). Possible values include: 'EC',
     'EC-HSM', 'RSA', 'RSA-HSM', 'oct'
    :type kty: str or ~azure.keyvault.models.JsonWebKeyType
    :param key_ops:
    :type key_ops: list[str]
    :param n: RSA modulus.
    :type n: bytes
    :param e: RSA public exponent.
    :type e: bytes
    :param d: RSA private exponent, or the D component of an EC private key.
    :type d: bytes
    :param dp: RSA private key parameter.
    :type dp: bytes
    :param dq: RSA private key parameter.
    :type dq: bytes
    :param qi: RSA private key parameter.
    :type qi: bytes
    :param p: RSA secret prime.
    :type p: bytes
    :param q: RSA secret prime, with p < q.
    :type q: bytes
    :param k: Symmetric key.
    :type k: bytes
    :param t: HSM Token, used with 'Bring Your Own Key'.
    :type t: bytes
    :param crv: Elliptic curve name. For valid values, see
     JsonWebKeyCurveName. Possible values include: 'P-256', 'P-384', 'P-521',
     'SECP256K1'
    :type crv: str or ~azure.keyvault.models.JsonWebKeyCurveName
    :param x: X component of an EC public key.
    :type x: bytes
    :param y: Y component of an EC public key.
    :type y: bytes
    """

    _attribute_map = {
        'kid': {'key': 'kid', 'type': 'str'},
        'kty': {'key': 'kty', 'type': 'str'},
        'key_ops': {'key': 'key_ops', 'type': '[str]'},
        'n': {'key': 'n', 'type': 'base64'},
        'e': {'key': 'e', 'type': 'base64'},
        'd': {'key': 'd', 'type': 'base64'},
        'dp': {'key': 'dp', 'type': 'base64'},
        'dq': {'key': 'dq', 'type': 'base64'},
        'qi': {'key': 'qi', 'type': 'base64'},
        'p': {'key': 'p', 'type': 'base64'},
        'q': {'key': 'q', 'type': 'base64'},
        'k': {'key': 'k', 'type': 'base64'},
        't': {'key': 'key_hsm', 'type': 'base64'},
        'crv': {'key': 'crv', 'type': 'str'},
        'x': {'key': 'x', 'type': 'base64'},
        'y': {'key': 'y', 'type': 'base64'},
    }

    def __init__(self, *, kid: str=None, kty=None, key_ops=None, n: bytes=None, e: bytes=None, d: bytes=None, dp: bytes=None, dq: bytes=None, qi: bytes=None, p: bytes=None, q: bytes=None, k: bytes=None, t: bytes=None, crv=None, x: bytes=None, y: bytes=None, **kwargs) -> None:
        super(JsonWebKey, self).__init__(**kwargs)
        self.kid = kid
        self.kty = kty
        self.key_ops = key_ops
        self.n = n
        self.e = e
        self.d = d
        self.dp = dp
        self.dq = dq
        self.qi = qi
        self.p = p
        self.q = q
        self.k = k
        self.t = t
        self.crv = crv
        self.x = x
        self.y = y