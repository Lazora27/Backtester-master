import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoFibonacci_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoFibonacci und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'AutoFibonacci': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
