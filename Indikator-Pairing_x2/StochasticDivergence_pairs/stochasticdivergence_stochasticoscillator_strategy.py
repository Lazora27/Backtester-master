import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_StochasticOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und StochasticOscillator
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'StochasticOscillator': {
                'class': StochasticOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticOscillator'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'StochasticOscillator': 1.0
        })
    )
