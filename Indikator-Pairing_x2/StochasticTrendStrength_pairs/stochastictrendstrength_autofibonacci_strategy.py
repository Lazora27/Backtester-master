import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_AutoFibonacci_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und AutoFibonacci
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'AutoFibonacci': 1.0
        })
    )
