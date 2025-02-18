import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_DOMDepth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und DOMDepth
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'DOMDepth': 1.0
        })
    )
