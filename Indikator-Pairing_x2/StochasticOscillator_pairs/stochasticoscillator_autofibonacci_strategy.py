import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticOscillator_AutoFibonacci_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticOscillator und AutoFibonacci
    """
    
    params = (
        ('indicators', {
            'StochasticOscillator': {
                'class': StochasticOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticOscillator'>
            },
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            }
        }),
        ('weights', {
            'StochasticOscillator': 1.0,
            'AutoFibonacci': 1.0
        })
    )
