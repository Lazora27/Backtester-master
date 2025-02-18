import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BidAskVolumeDelta_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BidAskVolumeDelta und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'BidAskVolumeDelta': {
                'class': BidAskVolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BidAskVolumeDelta'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'BidAskVolumeDelta': 1.0,
            'SmoothedCycle': 1.0
        })
    )
