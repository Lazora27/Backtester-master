import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_KeltnerChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und KeltnerChannels
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'KeltnerChannels': 1.0
        })
    )
