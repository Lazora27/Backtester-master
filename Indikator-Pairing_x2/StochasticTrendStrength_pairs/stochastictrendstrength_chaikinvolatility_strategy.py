import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_ChaikinVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und ChaikinVolatility
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'ChaikinVolatility': 1.0
        })
    )
