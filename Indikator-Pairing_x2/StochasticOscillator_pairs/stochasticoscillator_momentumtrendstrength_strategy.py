import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticOscillator_MomentumTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticOscillator und MomentumTrendStrength
    """
    
    params = (
        ('indicators', {
            'StochasticOscillator': {
                'class': StochasticOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticOscillator'>
            },
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            }
        }),
        ('weights', {
            'StochasticOscillator': 1.0,
            'MomentumTrendStrength': 1.0
        })
    )
