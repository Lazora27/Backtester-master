import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
