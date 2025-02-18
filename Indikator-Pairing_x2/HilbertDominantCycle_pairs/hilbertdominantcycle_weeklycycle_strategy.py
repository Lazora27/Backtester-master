import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HilbertDominantCycle_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HilbertDominantCycle und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'HilbertDominantCycle': 1.0,
            'WeeklyCycle': 1.0
        })
    )
