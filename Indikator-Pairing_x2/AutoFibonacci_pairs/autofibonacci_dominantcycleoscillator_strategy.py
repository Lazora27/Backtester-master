import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoFibonacci_DominantCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoFibonacci und DominantCycleOscillator
    """
    
    params = (
        ('indicators', {
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            },
            'DominantCycleOscillator': {
                'class': DominantCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DominantCycleOscillator'>
            }
        }),
        ('weights', {
            'AutoFibonacci': 1.0,
            'DominantCycleOscillator': 1.0
        })
    )
