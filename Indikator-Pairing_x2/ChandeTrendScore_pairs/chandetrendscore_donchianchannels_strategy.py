import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_DonchianChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und DonchianChannels
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'DonchianChannels': 1.0
        })
    )
