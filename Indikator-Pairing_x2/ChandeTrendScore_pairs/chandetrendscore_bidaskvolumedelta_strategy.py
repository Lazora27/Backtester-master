import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_BidAskVolumeDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und BidAskVolumeDelta
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'BidAskVolumeDelta': {
                'class': BidAskVolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BidAskVolumeDelta'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'BidAskVolumeDelta': 1.0
        })
    )
