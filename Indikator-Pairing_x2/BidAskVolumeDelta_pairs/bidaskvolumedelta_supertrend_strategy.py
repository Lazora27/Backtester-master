import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BidAskVolumeDelta_SuperTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BidAskVolumeDelta und SuperTrend
    """
    
    params = (
        ('indicators', {
            'BidAskVolumeDelta': {
                'class': BidAskVolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BidAskVolumeDelta'>
            },
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            }
        }),
        ('weights', {
            'BidAskVolumeDelta': 1.0,
            'SuperTrend': 1.0
        })
    )
