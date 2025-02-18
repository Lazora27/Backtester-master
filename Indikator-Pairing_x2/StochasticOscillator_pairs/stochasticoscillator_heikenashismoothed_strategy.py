import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticOscillator_HeikenAshiSmoothed_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticOscillator und HeikenAshiSmoothed
    """
    
    params = (
        ('indicators', {
            'StochasticOscillator': {
                'class': StochasticOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticOscillator'>
            },
            'HeikenAshiSmoothed': {
                'class': HeikenAshiSmoothed,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiSmoothed'>
            }
        }),
        ('weights', {
            'StochasticOscillator': 1.0,
            'HeikenAshiSmoothed': 1.0
        })
    )
