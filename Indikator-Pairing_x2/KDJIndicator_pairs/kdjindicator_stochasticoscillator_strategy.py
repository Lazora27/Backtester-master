import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KDJIndicator_StochasticOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KDJIndicator und StochasticOscillator
    """
    
    params = (
        ('indicators', {
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            },
            'StochasticOscillator': {
                'class': StochasticOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticOscillator'>
            }
        }),
        ('weights', {
            'KDJIndicator': 1.0,
            'StochasticOscillator': 1.0
        })
    )
