import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_StochasticTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und StochasticTrendStrength
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'StochasticTrendStrength': 1.0
        })
    )
