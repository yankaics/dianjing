
MESSAGE_TO_ID = {
    "UTCNotify": 10,
    "SyncRequest": 11,
    "SyncResponse": 12,
    "PingRequest": 13,
    "PingResponse": 14,
    "GetServerListRequest": 100,
    "GetServerListResponse": 101,
    "StartGameRequest": 102,
    "StartGameResponse": 103,
    "RegisterRequest": 200,
    "RegisterResponse": 201,
    "LoginRequest": 202,
    "LoginResponse": 203,
    "CharacterNotify": 300,
    "CreateCharacterRequest": 301,
    "CreateCharacterResponse": 302,
    "CharacterUploadAvatarRequest": 303,
    "CharacterUploadAvatarResponse": 304,
    "ClubNotify": 400,
    "CreateClubRequest": 401,
    "CreateClubResponse": 402,
    "StaffNotify": 500,
    "StaffRemoveNotify": 501,
    "StaffRecruitNotify": 520,
    "StaffRecruitRequest": 523,
    "StaffRecruitResponse": 524,
    "StaffEquipChangeRequest": 530,
    "StaffEquipChangeResponse": 531,
    "StaffLevelUpRequest": 532,
    "StaffLevelUpResponse": 533,
    "staffStepUpRequest": 534,
    "StaffStepUpResponse": 535,
    "StaffStarUpRequest": 536,
    "StaffStarUpResponse": 537,
    "StaffDestroyRequest": 538,
    "StaffDestroyResponse": 539,
    "ChallengeNotify": 700,
    "ChallengeStartRequest": 702,
    "ChallengeStartResponse": 703,
    "ChapterGetStarRewardRequest": 704,
    "ChapterGetStarRewardResponse": 705,
    "ChallengeMatchReportRequest": 706,
    "ChallengeMatchReportResponse": 707,
    "ChallengeSweepRequest": 710,
    "ChallengeSweepResponse": 711,
    "ChapterNotify": 720,
    "ChallengeResetRequest": 721,
    "ChallengeResetResponse": 722,
    "TaskNotify": 1100,
    "RandomEventDoneRequest": 1107,
    "RandomEventDoneResponse": 1108,
    "RandomEventNotify": 1109,
    "TaskDailyNotify": 1110,
    "TaskDailyGetRewardRequest": 1111,
    "TaskDailyGetRewardResponse": 1112,
    "FriendNotify": 1200,
    "FriendRemoveNotify": 1201,
    "FriendGetInfoRequest": 1202,
    "FriendGetInfoResponse": 1203,
    "FriendAddRequest": 1204,
    "FriendAddResponse": 1205,
    "FriendRemoveRequest": 1206,
    "FriendRemoveResponse": 1207,
    "FriendMatchRequest": 1208,
    "FriendMatchResponse": 1209,
    "FriendAcceptRequest": 1210,
    "FriendAcceptResponse": 1211,
    "FriendCandidatesRequest": 1212,
    "FriendCandidatesResponse": 1213,
    "MailNotify": 1300,
    "MailRemoveNotify": 1301,
    "MailSendRequest": 1302,
    "MailSendResponse": 1303,
    "MailOpenRequest": 1304,
    "MailOpenResponse": 1305,
    "MailDeleteRequest": 1306,
    "MailDeleteResponse": 1307,
    "MailGetAttachmentRequest": 1308,
    "MailGetAttachmentResponse": 1309,
    "ChatNotify": 1400,
    "ChatSendRequest": 1401,
    "ChatSendResponse": 1402,
    "NotificationNotify": 1500,
    "NotificationOpenRequest": 1501,
    "NotificationOpenResponse": 1502,
    "NotificationRemoveNotify": 1503,
    "NotificationDeleteRequest": 1504,
    "NotificationDeleteResponse": 1505,
    "FinanceStatisticsNotify": 1600,
    "LadderNotify": 1700,
    "LadderRefreshRequest": 1701,
    "LadderRefreshResponse": 1702,
    "LadderMatchRequest": 1703,
    "LadderMatchResponse": 1704,
    "LadderStoreNotify": 1705,
    "LadderStoreBuyRequest": 1706,
    "LadderStoreBuyResponse": 1707,
    "LadderLeaderBoardRequest": 1708,
    "LadderLeaderBoardResponse": 1709,
    "LadderStoreRefreshRequest": 1710,
    "LadderStoreRefreshResponse": 1711,
    "LadderMatchReportRequest": 1712,
    "LadderMatchReportResponse": 1713,
    "LadderBuyChallengeTimesRequest": 1714,
    "LadderBuyChallengeTimesResponse": 1715,
    "SponsorNotify": 1900,
    "SponsorRequest": 1903,
    "SponsorResponse": 1904,
    "SponsorGetIncomeRequest": 1905,
    "SponsorGetIncomeResponse": 1906,
    "ActivityCategoryNotify": 2000,
    "ActivitySignInNotify": 2001,
    "ActivitySignInRequest": 2002,
    "ActivitySignInResponse": 2003,
    "ActivityLoginRewardNotify": 2004,
    "ActivityLoginRewardRequest": 2005,
    "ActivityLoginRewardResponse": 2006,
    "ActiveValueNotify": 2100,
    "ActiveFunctionNotify": 2101,
    "ActiveValueGetRewardRequest": 2102,
    "ActiveValueGetRewardResponse": 2103,
    "ItemShopBuyRequest": 2300,
    "ItemShopBuyResponse": 2301,
    "StaffAuctionSellListNotify": 2700,
    "StaffAuctionSellRemoveNotify": 2701,
    "StaffAuctionSearchRequest": 2702,
    "StaffAuctionSearchResponse": 2703,
    "StaffAuctionSellRequest": 2704,
    "StaffAuctionSellResponse": 2705,
    "StaffAuctionCancelRequest": 2706,
    "StaffAuctionCancelResponse": 2707,
    "StaffAuctionBidingRequest": 2708,
    "StaffAuctionBiddingResponse": 2709,
    "StaffAuctionBidingListNotify": 2710,
    "StaffAuctionBidingRemoveNotify": 2711,
    "BroadcastNotify": 2800,
    "BagSlotsNotify": 3000,
    "BagSlotsRemoveNotify": 3001,
    "BagItemUseRequest": 3002,
    "BagItemUseResponse": 3003,
    "BagItemMergeRequest": 3004,
    "BagItemMergeResponse": 3005,
    "BagItemDestroyRequest": 3006,
    "BagItemDestroyResponse": 3007,
    "BagEquipmentLevelupRequest": 3010,
    "BagEquipmentLevelupResponse": 3011,
    "BagEquipmentDestroyRequest": 3012,
    "BagEquipmentDestroyResponse": 3013,
    "BagEquipmentLevelupConfirmRequest": 3014,
    "BagEquipmentLevelupConfirmResponse": 3015,
    "UnitNotify": 3100,
    "UnitLevelUpRequest": 3101,
    "UnitLevelUpResponse": 3102,
    "UnitStepUpRequest": 3103,
    "UnitStepUpResponse": 3104,
    "FormationNotify": 3200,
    "FormationSetStaffRequest": 3201,
    "FormationSetStaffResponse": 3202,
    "FormationSetUnitRequest": 3203,
    "FormationSetUnitResponse": 3204,
    "FormationMoveSlotRequest": 3205,
    "FormationMoveSlotResponse": 3206,
    "TalentNotify": 3300,
    "TalentLevelUpRequest": 3301,
    "TalentLevelUpResponse": 3302,
    "TalentResetTalentRequest": 3303,
    "TalentResetTalentResponse": 3304,
    "DungeonNotify": 3400,
    "DungeonMatchRequest": 3401,
    "DungeonMatchResponse": 3402,
    "DungeonMatchReportRequest": 3403,
    "DungeonMatchReportResponse": 3404,
    "DungeonBuyTimesRequest": 3405,
    "DungeonBuyTimesResponse": 3406,
    "ArenaNotify": 3500,
    "ArenaRefreshRequest": 3501,
    "ArenaRefreshResponse": 3502,
    "ArenaLeaderBoardRequest": 3503,
    "ArenaLeaderBoardResponse": 3504,
    "ArenaHonorStatusNotify": 3505,
    "ArenaHonorGetRewardRequest": 3507,
    "ArenaHonorGetRewardResponse": 3508,
    "ArenaMatchStartReqeust": 3509,
    "ArenaMatchStartResponse": 3510,
    "ArenaMatchReportReqeust": 3511,
    "ArenaMatchReportResponse": 3512,
    "ArenaMatchLogNotify": 3513,
    "ArenaBuyTimesRequest": 3514,
    "ArenaBuyTimesResponse": 3515,
    "TowerNotify": 3600,
    "TowerMatchStartRequest": 3601,
    "TowerMatchStartResponse": 3602,
    "TowerMatchReportReqeust": 3603,
    "TowerMatchReportResponse": 3604,
    "TowerResetRequest": 3605,
    "TowerResetResponse": 3606,
    "TowerTurnTableRequest": 3609,
    "TowerTurnTableResponse": 3610,
    "TowerSweepRequest": 3611,
    "TowerSweepResponse": 3612,
    "TowerSweepFinishRequest": 3613,
    "TowerSweepFinishResponse": 3614,
    "TerritoryNotify": 3700,
    "TerritoryTrainingStartReqeust": 3703,
    "TerritoryTrainingStartResponse": 3704,
    "TerritoryTrainingGetRewardReqeust": 3705,
    "TerritoryTrainingGetRewardResponse": 3706,
    "TerritoryStoreNotify": 3710,
    "TerritoryStoreBuyRequest": 3711,
    "TerritoryStoreBuyResponse": 3712,
    "TerritoryFriendListRequest": 3713,
    "TerritoryFriendListResponse": 3714,
    "TerritoryFriendHelpRequest": 3717,
    "TerritoryFriendHelpResponse": 3718,
    "TerritoryMatchReportRequest": 3719,
    "TerritoryMatchReportResponse": 3720,
    "StoreNotify": 3800,
    "StoreBuyRequest": 3801,
    "StoreBuyResponse": 3802,
    "StoreRefreshRequest": 3803,
    "StoreRefreshResponse": 3804,
    "StoreAutoRefreshRequest": 3805,
    "StoreAutoRefreshResponse": 3806,
    "VIPNotify": 3900,
    "VIPBuyRewardRequest": 3901,
    "VIPBuyRewardResponse": 3902,
    "CollectionNotify": 4000,
    "EnergyNotify": 4100,
    "EnergyBuyRequest": 4101,
    "EnergyBuyResponse": 4102,
}

ID_TO_MESSAGE = {
    10: "UTCNotify",
    11: "SyncRequest",
    12: "SyncResponse",
    13: "PingRequest",
    14: "PingResponse",
    100: "GetServerListRequest",
    101: "GetServerListResponse",
    102: "StartGameRequest",
    103: "StartGameResponse",
    200: "RegisterRequest",
    201: "RegisterResponse",
    202: "LoginRequest",
    203: "LoginResponse",
    300: "CharacterNotify",
    301: "CreateCharacterRequest",
    302: "CreateCharacterResponse",
    303: "CharacterUploadAvatarRequest",
    304: "CharacterUploadAvatarResponse",
    400: "ClubNotify",
    401: "CreateClubRequest",
    402: "CreateClubResponse",
    500: "StaffNotify",
    501: "StaffRemoveNotify",
    520: "StaffRecruitNotify",
    523: "StaffRecruitRequest",
    524: "StaffRecruitResponse",
    530: "StaffEquipChangeRequest",
    531: "StaffEquipChangeResponse",
    532: "StaffLevelUpRequest",
    533: "StaffLevelUpResponse",
    534: "staffStepUpRequest",
    535: "StaffStepUpResponse",
    536: "StaffStarUpRequest",
    537: "StaffStarUpResponse",
    538: "StaffDestroyRequest",
    539: "StaffDestroyResponse",
    700: "ChallengeNotify",
    702: "ChallengeStartRequest",
    703: "ChallengeStartResponse",
    704: "ChapterGetStarRewardRequest",
    705: "ChapterGetStarRewardResponse",
    706: "ChallengeMatchReportRequest",
    707: "ChallengeMatchReportResponse",
    710: "ChallengeSweepRequest",
    711: "ChallengeSweepResponse",
    720: "ChapterNotify",
    721: "ChallengeResetRequest",
    722: "ChallengeResetResponse",
    1100: "TaskNotify",
    1107: "RandomEventDoneRequest",
    1108: "RandomEventDoneResponse",
    1109: "RandomEventNotify",
    1110: "TaskDailyNotify",
    1111: "TaskDailyGetRewardRequest",
    1112: "TaskDailyGetRewardResponse",
    1200: "FriendNotify",
    1201: "FriendRemoveNotify",
    1202: "FriendGetInfoRequest",
    1203: "FriendGetInfoResponse",
    1204: "FriendAddRequest",
    1205: "FriendAddResponse",
    1206: "FriendRemoveRequest",
    1207: "FriendRemoveResponse",
    1208: "FriendMatchRequest",
    1209: "FriendMatchResponse",
    1210: "FriendAcceptRequest",
    1211: "FriendAcceptResponse",
    1212: "FriendCandidatesRequest",
    1213: "FriendCandidatesResponse",
    1300: "MailNotify",
    1301: "MailRemoveNotify",
    1302: "MailSendRequest",
    1303: "MailSendResponse",
    1304: "MailOpenRequest",
    1305: "MailOpenResponse",
    1306: "MailDeleteRequest",
    1307: "MailDeleteResponse",
    1308: "MailGetAttachmentRequest",
    1309: "MailGetAttachmentResponse",
    1400: "ChatNotify",
    1401: "ChatSendRequest",
    1402: "ChatSendResponse",
    1500: "NotificationNotify",
    1501: "NotificationOpenRequest",
    1502: "NotificationOpenResponse",
    1503: "NotificationRemoveNotify",
    1504: "NotificationDeleteRequest",
    1505: "NotificationDeleteResponse",
    1600: "FinanceStatisticsNotify",
    1700: "LadderNotify",
    1701: "LadderRefreshRequest",
    1702: "LadderRefreshResponse",
    1703: "LadderMatchRequest",
    1704: "LadderMatchResponse",
    1705: "LadderStoreNotify",
    1706: "LadderStoreBuyRequest",
    1707: "LadderStoreBuyResponse",
    1708: "LadderLeaderBoardRequest",
    1709: "LadderLeaderBoardResponse",
    1710: "LadderStoreRefreshRequest",
    1711: "LadderStoreRefreshResponse",
    1712: "LadderMatchReportRequest",
    1713: "LadderMatchReportResponse",
    1714: "LadderBuyChallengeTimesRequest",
    1715: "LadderBuyChallengeTimesResponse",
    1900: "SponsorNotify",
    1903: "SponsorRequest",
    1904: "SponsorResponse",
    1905: "SponsorGetIncomeRequest",
    1906: "SponsorGetIncomeResponse",
    2000: "ActivityCategoryNotify",
    2001: "ActivitySignInNotify",
    2002: "ActivitySignInRequest",
    2003: "ActivitySignInResponse",
    2004: "ActivityLoginRewardNotify",
    2005: "ActivityLoginRewardRequest",
    2006: "ActivityLoginRewardResponse",
    2100: "ActiveValueNotify",
    2101: "ActiveFunctionNotify",
    2102: "ActiveValueGetRewardRequest",
    2103: "ActiveValueGetRewardResponse",
    2300: "ItemShopBuyRequest",
    2301: "ItemShopBuyResponse",
    2700: "StaffAuctionSellListNotify",
    2701: "StaffAuctionSellRemoveNotify",
    2702: "StaffAuctionSearchRequest",
    2703: "StaffAuctionSearchResponse",
    2704: "StaffAuctionSellRequest",
    2705: "StaffAuctionSellResponse",
    2706: "StaffAuctionCancelRequest",
    2707: "StaffAuctionCancelResponse",
    2708: "StaffAuctionBidingRequest",
    2709: "StaffAuctionBiddingResponse",
    2710: "StaffAuctionBidingListNotify",
    2711: "StaffAuctionBidingRemoveNotify",
    2800: "BroadcastNotify",
    3000: "BagSlotsNotify",
    3001: "BagSlotsRemoveNotify",
    3002: "BagItemUseRequest",
    3003: "BagItemUseResponse",
    3004: "BagItemMergeRequest",
    3005: "BagItemMergeResponse",
    3006: "BagItemDestroyRequest",
    3007: "BagItemDestroyResponse",
    3010: "BagEquipmentLevelupRequest",
    3011: "BagEquipmentLevelupResponse",
    3012: "BagEquipmentDestroyRequest",
    3013: "BagEquipmentDestroyResponse",
    3014: "BagEquipmentLevelupConfirmRequest",
    3015: "BagEquipmentLevelupConfirmResponse",
    3100: "UnitNotify",
    3101: "UnitLevelUpRequest",
    3102: "UnitLevelUpResponse",
    3103: "UnitStepUpRequest",
    3104: "UnitStepUpResponse",
    3200: "FormationNotify",
    3201: "FormationSetStaffRequest",
    3202: "FormationSetStaffResponse",
    3203: "FormationSetUnitRequest",
    3204: "FormationSetUnitResponse",
    3205: "FormationMoveSlotRequest",
    3206: "FormationMoveSlotResponse",
    3300: "TalentNotify",
    3301: "TalentLevelUpRequest",
    3302: "TalentLevelUpResponse",
    3303: "TalentResetTalentRequest",
    3304: "TalentResetTalentResponse",
    3400: "DungeonNotify",
    3401: "DungeonMatchRequest",
    3402: "DungeonMatchResponse",
    3403: "DungeonMatchReportRequest",
    3404: "DungeonMatchReportResponse",
    3405: "DungeonBuyTimesRequest",
    3406: "DungeonBuyTimesResponse",
    3500: "ArenaNotify",
    3501: "ArenaRefreshRequest",
    3502: "ArenaRefreshResponse",
    3503: "ArenaLeaderBoardRequest",
    3504: "ArenaLeaderBoardResponse",
    3505: "ArenaHonorStatusNotify",
    3507: "ArenaHonorGetRewardRequest",
    3508: "ArenaHonorGetRewardResponse",
    3509: "ArenaMatchStartReqeust",
    3510: "ArenaMatchStartResponse",
    3511: "ArenaMatchReportReqeust",
    3512: "ArenaMatchReportResponse",
    3513: "ArenaMatchLogNotify",
    3514: "ArenaBuyTimesRequest",
    3515: "ArenaBuyTimesResponse",
    3600: "TowerNotify",
    3601: "TowerMatchStartRequest",
    3602: "TowerMatchStartResponse",
    3603: "TowerMatchReportReqeust",
    3604: "TowerMatchReportResponse",
    3605: "TowerResetRequest",
    3606: "TowerResetResponse",
    3609: "TowerTurnTableRequest",
    3610: "TowerTurnTableResponse",
    3611: "TowerSweepRequest",
    3612: "TowerSweepResponse",
    3613: "TowerSweepFinishRequest",
    3614: "TowerSweepFinishResponse",
    3700: "TerritoryNotify",
    3703: "TerritoryTrainingStartReqeust",
    3704: "TerritoryTrainingStartResponse",
    3705: "TerritoryTrainingGetRewardReqeust",
    3706: "TerritoryTrainingGetRewardResponse",
    3710: "TerritoryStoreNotify",
    3711: "TerritoryStoreBuyRequest",
    3712: "TerritoryStoreBuyResponse",
    3713: "TerritoryFriendListRequest",
    3714: "TerritoryFriendListResponse",
    3717: "TerritoryFriendHelpRequest",
    3718: "TerritoryFriendHelpResponse",
    3719: "TerritoryMatchReportRequest",
    3720: "TerritoryMatchReportResponse",
    3800: "StoreNotify",
    3801: "StoreBuyRequest",
    3802: "StoreBuyResponse",
    3803: "StoreRefreshRequest",
    3804: "StoreRefreshResponse",
    3805: "StoreAutoRefreshRequest",
    3806: "StoreAutoRefreshResponse",
    3900: "VIPNotify",
    3901: "VIPBuyRewardRequest",
    3902: "VIPBuyRewardResponse",
    4000: "CollectionNotify",
    4100: "EnergyNotify",
    4101: "EnergyBuyRequest",
    4102: "EnergyBuyResponse",
}

PATH_TO_REQUEST = {
    "/game/sync/": ["common", "SyncRequest"],
    "/game/ping/": ["common", "PingRequest"],
    "/game/servers/": ["server", "GetServerListRequest"],
    "/game/start/": ["server", "StartGameRequest"],
    "/game/account/register/": ["account", "RegisterRequest"],
    "/game/account/login/": ["account", "LoginRequest"],
    "/game/character/create/": ["character", "CreateCharacterRequest"],
    "/game/character/avatar/upload/": ["character", "CharacterUploadAvatarRequest"],
    "/game/club/create/": ["club", "CreateClubRequest"],
    "/game/staff/recruit/": ["staff", "StaffRecruitRequest"],
    "/game/staff/equipchange/": ["staff", "StaffEquipChangeRequest"],
    "/game/staff/levelup/": ["staff", "StaffLevelUpRequest"],
    "/game/staff/stepup/": ["staff", "staffStepUpRequest"],
    "/game/staff/starup/": ["staff", "StaffStarUpRequest"],
    "/game/staff/destroy/": ["staff", "StaffDestroyRequest"],
    "/game/challenge/start/": ["challenge", "ChallengeStartRequest"],
    "/game/challenge/chapter/reward/": ["challenge", "ChapterGetStarRewardRequest"],
    "/game/challenge/report/": ["challenge", "ChallengeMatchReportRequest"],
    "/game/challenge/sweep/": ["challenge", "ChallengeSweepRequest"],
    "/game/challenge/reset/": ["challenge", "ChallengeResetRequest"],
    "/game/randomevent/done/": ["task", "RandomEventDoneRequest"],
    "/game/taskdaily/getreward/": ["task", "TaskDailyGetRewardRequest"],
    "/game/friend/info/": ["friend", "FriendGetInfoRequest"],
    "/game/friend/add/": ["friend", "FriendAddRequest"],
    "/game/friend/remove/": ["friend", "FriendRemoveRequest"],
    "/game/friend/match/": ["friend", "FriendMatchRequest"],
    "/game/friend/accept/": ["friend", "FriendAcceptRequest"],
    "/game/friend/candidates/": ["friend", "FriendCandidatesRequest"],
    "/game/mail/send/": ["mail", "MailSendRequest"],
    "/game/mail/open/": ["mail", "MailOpenRequest"],
    "/game/mail/delete/": ["mail", "MailDeleteRequest"],
    "/game/mail/getattachment/": ["mail", "MailGetAttachmentRequest"],
    "/game/chat/send/": ["chat", "ChatSendRequest"],
    "/game/notification/open/": ["notification", "NotificationOpenRequest"],
    "/game/notification/delete/": ["notification", "NotificationDeleteRequest"],
    "/game/ladder/refresh/": ["ladder", "LadderRefreshRequest"],
    "/game/ladder/match/": ["ladder", "LadderMatchRequest"],
    "/game/ladder/store/buy/": ["ladder", "LadderStoreBuyRequest"],
    "/game/ladder/leaderboard/": ["ladder", "LadderLeaderBoardRequest"],
    "/game/ladder/store/refresh/": ["ladder", "LadderStoreRefreshRequest"],
    "/game/ladder/store/report/": ["ladder", "LadderMatchReportRequest"],
    "/game/ladder/buy/": ["ladder", "LadderBuyChallengeTimesRequest"],
    "/game/sponsor/": ["spread", "SponsorRequest"],
    "/game/sponsor/getincome/": ["spread", "SponsorGetIncomeRequest"],
    "/game/signin/": ["activity", "ActivitySignInRequest"],
    "/game/activity/loginreward/": ["activity", "ActivityLoginRewardRequest"],
    "/game/activevalue/getreward/": ["active_value", "ActiveValueGetRewardRequest"],
    "/game/itemshop/buy/": ["shop", "ItemShopBuyRequest"],
    "/game/auction/search/": ["auction", "StaffAuctionSearchRequest"],
    "/game/auction/sell/": ["auction", "StaffAuctionSellRequest"],
    "/game/auction/cancel/": ["auction", "StaffAuctionCancelRequest"],
    "/game/auction/bidding/": ["auction", "StaffAuctionBidingRequest"],
    "/game/bagitem/use/": ["bag", "BagItemUseRequest"],
    "/game/bagitem/merge/": ["bag", "BagItemMergeRequest"],
    "/game/bagitem/destroy/": ["bag", "BagItemDestroyRequest"],
    "/game/bagequipment/levelup/": ["bag", "BagEquipmentLevelupRequest"],
    "/game/bagequipment/destroy/": ["bag", "BagEquipmentDestroyRequest"],
    "/game/bagequipment/levelup/confirm/": ["bag", "BagEquipmentLevelupConfirmRequest"],
    "/game/unit/levelup/": ["unit", "UnitLevelUpRequest"],
    "/game/unit/stepup/": ["unit", "UnitStepUpRequest"],
    "/game/formation/setstaff/": ["formation", "FormationSetStaffRequest"],
    "/game/formation/setunit/": ["formation", "FormationSetUnitRequest"],
    "/game/formation/moveslot/": ["formation", "FormationMoveSlotRequest"],
    "/game/talent/levelup/": ["talent", "TalentLevelUpRequest"],
    "/game/talent/reset/": ["talent", "TalentResetTalentRequest"],
    "/game/dungeon/start/": ["dungeon", "DungeonMatchRequest"],
    "/game/dungeon/report/": ["dungeon", "DungeonMatchReportRequest"],
    "/game/dungeon/buytimes/": ["dungeon", "DungeonBuyTimesRequest"],
    "/game/arena/refresh/": ["arena", "ArenaRefreshRequest"],
    "/game/arena/leaderboard/": ["arena", "ArenaLeaderBoardRequest"],
    "/game/arena/honorreward/": ["arena", "ArenaHonorGetRewardRequest"],
    "/game/arena/matchstart/": ["arena", "ArenaMatchStartReqeust"],
    "/game/arena/matchreport/": ["arena", "ArenaMatchReportReqeust"],
    "/game/arena/buytimes/": ["arena", "ArenaBuyTimesRequest"],
    "/game/tower/matchstart/": ["tower", "TowerMatchStartRequest"],
    "/game/tower/matchreport/": ["tower", "TowerMatchReportReqeust"],
    "/game/tower/reset/": ["tower", "TowerResetRequest"],
    "/game/tower/turntable/": ["tower", "TowerTurnTableRequest"],
    "/game/tower/sweep/": ["tower", "TowerSweepRequest"],
    "/game/tower/sweepfinish/": ["tower", "TowerSweepFinishRequest"],
    "/game/territory/start/": ["territory", "TerritoryTrainingStartReqeust"],
    "/game/territory/getreward/": ["territory", "TerritoryTrainingGetRewardReqeust"],
    "/game/territory/store/buy/": ["territory", "TerritoryStoreBuyRequest"],
    "/game/territory/friend/list/": ["territory", "TerritoryFriendListRequest"],
    "/game/territory/friend/help/": ["territory", "TerritoryFriendHelpRequest"],
    "/game/territory/friend/report/": ["territory", "TerritoryMatchReportRequest"],
    "/game/store/buy/": ["store", "StoreBuyRequest"],
    "/game/store/refresh/": ["store", "StoreRefreshRequest"],
    "/game/store/autorefresh/": ["store", "StoreAutoRefreshRequest"],
    "/game/vip/buyreward/": ["vip", "VIPBuyRewardRequest"],
    "/game/energy/buy/": ["energy", "EnergyBuyRequest"],
}

PATH_TO_RESPONSE = {
    "/game/sync/": ["common", "SyncResponse"],
    "/game/sync/": ["common", "PingResponse"],
    "/game/servers/": ["server", "GetServerListResponse"],
    "/game/start/": ["server", "StartGameResponse"],
    "/game/account/register/": ["account", "RegisterResponse"],
    "/game/account/login/": ["account", "LoginResponse"],
    "/game/character/create/": ["character", "CreateCharacterResponse"],
    "/game/character/avatar/upload/": ["character", "CharacterUploadAvatarResponse"],
    "/game/club/create/": ["club", "CreateClubResponse"],
    "/game/staff/recruit/": ["staff", "StaffRecruitResponse"],
    "/game/staff/equipchange/": ["staff", "StaffEquipChangeResponse"],
    "/game/staff/levelup/": ["staff", "StaffLevelUpResponse"],
    "/game/staff/stepup/": ["staff", "StaffStepUpResponse"],
    "/game/staff/starup/": ["staff", "StaffStarUpResponse"],
    "/game/staff/destroy/": ["staff", "StaffDestroyResponse"],
    "/game/challenge/start/": ["challenge", "ChallengeStartResponse"],
    "/game/challenge/chapter/reward/": ["challenge", "ChapterGetStarRewardResponse"],
    "/game/challenge/report/": ["challenge", "ChallengeMatchReportResponse"],
    "/game/challenge/sweep/": ["challenge", "ChallengeSweepResponse"],
    "/game/challenge/reset/": ["challenge", "ChallengeResetResponse"],
    "/game/randomevent/done/": ["task", "RandomEventDoneResponse"],
    "/game/taskdaily/getreward/": ["task", "TaskDailyGetRewardResponse"],
    "/game/friend/info/": ["friend", "FriendGetInfoResponse"],
    "/game/friend/add/": ["friend", "FriendAddResponse"],
    "/game/friend/remove/": ["friend", "FriendRemoveResponse"],
    "/game/friend/match/": ["friend", "FriendMatchResponse"],
    "/game/friend/accept/": ["friend", "FriendAcceptResponse"],
    "/game/friend/candidates/": ["friend", "FriendCandidatesResponse"],
    "/game/mail/send/": ["mail", "MailSendResponse"],
    "/game/mail/open/": ["mail", "MailOpenResponse"],
    "/game/mail/delete/": ["mail", "MailDeleteResponse"],
    "/game/mail/getattachment/": ["mail", "MailGetAttachmentResponse"],
    "/game/chat/send/": ["chat", "ChatSendResponse"],
    "/game/notification/open/": ["notification", "NotificationOpenResponse"],
    "/game/notification/delete/": ["notification", "NotificationDeleteResponse"],
    "/game/ladder/refresh/": ["ladder", "LadderRefreshResponse"],
    "/game/ladder/match/": ["ladder", "LadderMatchResponse"],
    "/game/ladder/store/buy/": ["ladder", "LadderStoreBuyResponse"],
    "/game/ladder/leaderboard/": ["ladder", "LadderLeaderBoardResponse"],
    "/game/ladder/store/refresh/": ["ladder", "LadderStoreRefreshResponse"],
    "/game/ladder/store/report/": ["ladder", "LadderMatchReportResponse"],
    "/game/ladder/buy/": ["ladder", "LadderBuyChallengeTimesResponse"],
    "/game/sponsor/": ["spread", "SponsorResponse"],
    "/game/sponsor/getincome/": ["spread", "SponsorGetIncomeResponse"],
    "/game/signin/": ["activity", "ActivitySignInResponse"],
    "/game/activity/loginreward/": ["activity", "ActivityLoginRewardResponse"],
    "/game/activevalue/getreward/": ["active_value", "ActiveValueGetRewardResponse"],
    "/game/itemshop/buy/": ["shop", "ItemShopBuyResponse"],
    "/game/auction/search/": ["auction", "StaffAuctionSearchResponse"],
    "/game/auction/sell/": ["auction", "StaffAuctionSellResponse"],
    "/game/auction/cancel/": ["auction", "StaffAuctionCancelResponse"],
    "/game/auction/bidding/": ["auction", "StaffAuctionBiddingResponse"],
    "/game/bagitem/use/": ["bag", "BagItemUseResponse"],
    "/game/bagitem/merge/": ["bag", "BagItemMergeResponse"],
    "/game/bagitem/destroy/": ["bag", "BagItemDestroyResponse"],
    "/game/bagequipment/levelup/": ["bag", "BagEquipmentLevelupResponse"],
    "/game/bagequipment/destroy/": ["bag", "BagEquipmentDestroyResponse"],
    "/game/bagequipment/levelup/confirm/": ["bag", "BagEquipmentLevelupConfirmResponse"],
    "/game/unit/levelup/": ["unit", "UnitLevelUpResponse"],
    "/game/unit/stepup/": ["unit", "UnitStepUpResponse"],
    "/game/formation/setstaff/": ["formation", "FormationSetStaffResponse"],
    "/game/formation/setunit/": ["formation", "FormationSetUnitResponse"],
    "/game/formation/moveslot/": ["formation", "FormationMoveSlotResponse"],
    "/game/talent/levelup/": ["talent", "TalentLevelUpResponse"],
    "/game/talent/reset/": ["talent", "TalentResetTalentResponse"],
    "/game/dungeon/start/": ["dungeon", "DungeonMatchResponse"],
    "/game/dungeon/report/": ["dungeon", "DungeonMatchReportResponse"],
    "/game/dungeon/buytimes/": ["dungeon", "DungeonBuyTimesResponse"],
    "/game/arena/refresh/": ["arena", "ArenaRefreshResponse"],
    "/game/arena/leaderboard/": ["arena", "ArenaLeaderBoardResponse"],
    "/game/arena/honorreward/": ["arena", "ArenaHonorGetRewardResponse"],
    "/game/arena/matchstart/": ["arena", "ArenaMatchStartResponse"],
    "/game/arena/matchreport/": ["arena", "ArenaMatchReportResponse"],
    "/game/arena/buytimes/": ["arena", "ArenaBuyTimesResponse"],
    "/game/tower/matchstart/": ["tower", "TowerMatchStartResponse"],
    "/game/tower/matchreport/": ["tower", "TowerMatchReportResponse"],
    "/game/tower/reset/": ["tower", "TowerResetResponse"],
    "/game/tower/turntable/": ["tower", "TowerTurnTableResponse"],
    "/game/tower/sweep/": ["tower", "TowerSweepResponse"],
    "/game/tower/sweepfinish/": ["tower", "TowerSweepFinishResponse"],
    "/game/territory/start/": ["territory", "TerritoryTrainingStartResponse"],
    "/game/territory/getreward/": ["territory", "TerritoryTrainingGetRewardResponse"],
    "/game/territory/store/buy/": ["territory", "TerritoryStoreBuyResponse"],
    "/game/territory/friend/list/": ["territory", "TerritoryFriendListResponse"],
    "/game/territory/friend/help/": ["territory", "TerritoryFriendHelpResponse"],
    "/game/territory/friend/report/": ["territory", "TerritoryMatchReportResponse"],
    "/game/store/buy/": ["store", "StoreBuyResponse"],
    "/game/store/refresh/": ["store", "StoreRefreshResponse"],
    "/game/store/autorefresh/": ["store", "StoreAutoRefreshResponse"],
    "/game/vip/buyreward/": ["vip", "VIPBuyRewardResponse"],
    "/game/energy/buy/": ["energy", "EnergyBuyResponse"],
}
