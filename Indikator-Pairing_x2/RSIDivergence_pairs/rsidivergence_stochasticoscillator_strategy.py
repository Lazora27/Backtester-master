import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_StochasticOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und StochasticOscillator
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'StochasticOscillator': {
                'class': StochasticOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticOscillator'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'StochasticOscillator': 1.0
        })
    )
