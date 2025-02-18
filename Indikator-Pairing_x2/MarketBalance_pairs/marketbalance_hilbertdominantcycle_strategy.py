import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketBalance_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketBalance und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'MarketBalance': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
