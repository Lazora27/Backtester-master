import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_DecyclerOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und DecyclerOscillator
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'DecyclerOscillator': {
                'class': DecyclerOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DecyclerOscillator'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'DecyclerOscillator': 1.0
        })
    )
