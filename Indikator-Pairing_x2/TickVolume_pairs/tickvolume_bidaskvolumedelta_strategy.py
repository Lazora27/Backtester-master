import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_BidAskVolumeDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und BidAskVolumeDelta
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'BidAskVolumeDelta': {
                'class': BidAskVolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BidAskVolumeDelta'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'BidAskVolumeDelta': 1.0
        })
    )
