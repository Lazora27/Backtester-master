import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketOrderFlow_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketOrderFlow und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'MarketOrderFlow': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
