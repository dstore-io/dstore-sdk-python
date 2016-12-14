#!/usr/bin/env python
# -*- coding: utf-8 -*-
class DstoreMetadata:
    ENGINE_RETURN_STATUS_KEY = 'dstore-engine-returnstatus'
    USERNAME_KEY = 'dstore-username'
    PASSWORD_KEY = 'dstore-password'
    ACCESS_TOKEN_KEY = 'dstore-accesstoken'

    @staticmethod
    def buildTrailingMetadata(metadata):
        metadata_dict = {}
        for current_metadata in metadata:
            metadata_dict[current_metadata[0]] = current_metadata[1]
        return metadata_dict