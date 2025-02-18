import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticOscillator_DOMDepth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticOscillator und DOMDepth
    """
    
    params = (
        ('indicators', {
            'StochasticOscillator': {
                'class': StochasticOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticOscillator'>
            },
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            }
        }),
        ('weights', {
            'StochasticOscillator': 1.0,
            'DOMDepth': 1.0
        })
    )
