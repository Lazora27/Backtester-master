import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BidAskVolumeDelta_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BidAskVolumeDelta und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'BidAskVolumeDelta': {
                'class': BidAskVolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BidAskVolumeDelta'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'BidAskVolumeDelta': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
