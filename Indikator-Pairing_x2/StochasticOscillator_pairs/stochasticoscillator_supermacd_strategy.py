import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticOscillator_SuperMACD_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticOscillator und SuperMACD
    """
    
    params = (
        ('indicators', {
            'StochasticOscillator': {
                'class': StochasticOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticOscillator'>
            },
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            }
        }),
        ('weights', {
            'StochasticOscillator': 1.0,
            'SuperMACD': 1.0
        })
    )
