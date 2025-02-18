import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BidAskVolumeDelta_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BidAskVolumeDelta und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'BidAskVolumeDelta': {
                'class': BidAskVolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BidAskVolumeDelta'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'BidAskVolumeDelta': 1.0,
            'WeightedCycle': 1.0
        })
    )
