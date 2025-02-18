import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticOscillator_UltimateOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticOscillator und UltimateOscillator
    """
    
    params = (
        ('indicators', {
            'StochasticOscillator': {
                'class': StochasticOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticOscillator'>
            },
            'UltimateOscillator': {
                'class': UltimateOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UltimateOscillator1'>
            }
        }),
        ('weights', {
            'StochasticOscillator': 1.0,
            'UltimateOscillator': 1.0
        })
    )
