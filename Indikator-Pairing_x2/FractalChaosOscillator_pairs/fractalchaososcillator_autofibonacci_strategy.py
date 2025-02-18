import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FractalChaosOscillator_AutoFibonacci_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FractalChaosOscillator und AutoFibonacci
    """
    
    params = (
        ('indicators', {
            'FractalChaosOscillator': {
                'class': FractalChaosOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FractalChaosOscillator'>
            },
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            }
        }),
        ('weights', {
            'FractalChaosOscillator': 1.0,
            'AutoFibonacci': 1.0
        })
    )
