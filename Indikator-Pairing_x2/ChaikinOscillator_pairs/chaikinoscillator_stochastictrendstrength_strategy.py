import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinOscillator_StochasticTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinOscillator und StochasticTrendStrength
    """
    
    params = (
        ('indicators', {
            'ChaikinOscillator': {
                'class': ChaikinOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinOscillator'>
            },
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            }
        }),
        ('weights', {
            'ChaikinOscillator': 1.0,
            'StochasticTrendStrength': 1.0
        })
    )
