import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_StochasticTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und StochasticTrendStrength
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'StochasticTrendStrength': 1.0
        })
    )
