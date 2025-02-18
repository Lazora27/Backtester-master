import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HilbertDominantCycle_PriceCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HilbertDominantCycle und PriceCycleOscillator
    """
    
    params = (
        ('indicators', {
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            },
            'PriceCycleOscillator': {
                'class': PriceCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceCycleOscillator'>
            }
        }),
        ('weights', {
            'HilbertDominantCycle': 1.0,
            'PriceCycleOscillator': 1.0
        })
    )
