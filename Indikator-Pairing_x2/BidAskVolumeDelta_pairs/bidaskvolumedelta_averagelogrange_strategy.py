import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BidAskVolumeDelta_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BidAskVolumeDelta und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'BidAskVolumeDelta': {
                'class': BidAskVolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BidAskVolumeDelta'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'BidAskVolumeDelta': 1.0,
            'AverageLogRange': 1.0
        })
    )
