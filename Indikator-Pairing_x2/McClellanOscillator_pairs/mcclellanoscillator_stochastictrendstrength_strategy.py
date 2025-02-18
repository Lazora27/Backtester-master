import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanOscillator_StochasticTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanOscillator und StochasticTrendStrength
    """
    
    params = (
        ('indicators', {
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            },
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            }
        }),
        ('weights', {
            'McClellanOscillator': 1.0,
            'StochasticTrendStrength': 1.0
        })
    )
