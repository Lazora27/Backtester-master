import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticOscillator_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticOscillator und BarStrength
    """
    
    params = (
        ('indicators', {
            'StochasticOscillator': {
                'class': StochasticOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticOscillator'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'StochasticOscillator': 1.0,
            'BarStrength': 1.0
        })
    )
