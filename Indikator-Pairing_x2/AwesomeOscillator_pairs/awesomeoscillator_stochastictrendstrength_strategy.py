import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AwesomeOscillator_StochasticTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AwesomeOscillator und StochasticTrendStrength
    """
    
    params = (
        ('indicators', {
            'AwesomeOscillator': {
                'class': AwesomeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AwesomeOscillator1'>
            },
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            }
        }),
        ('weights', {
            'AwesomeOscillator': 1.0,
            'StochasticTrendStrength': 1.0
        })
    )
