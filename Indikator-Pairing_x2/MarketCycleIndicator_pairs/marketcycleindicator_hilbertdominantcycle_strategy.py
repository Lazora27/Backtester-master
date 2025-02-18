import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketCycleIndicator_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketCycleIndicator und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'MarketCycleIndicator': {
                'class': MarketCycleIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketCycleIndicator'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'MarketCycleIndicator': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
