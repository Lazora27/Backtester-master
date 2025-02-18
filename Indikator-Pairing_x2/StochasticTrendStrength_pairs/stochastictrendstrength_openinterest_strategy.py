import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und OpenInterest
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'OpenInterest': 1.0
        })
    )
