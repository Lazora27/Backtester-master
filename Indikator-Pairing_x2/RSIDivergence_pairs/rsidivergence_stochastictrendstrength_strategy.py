import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_StochasticTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und StochasticTrendStrength
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'StochasticTrendStrength': 1.0
        })
    )
