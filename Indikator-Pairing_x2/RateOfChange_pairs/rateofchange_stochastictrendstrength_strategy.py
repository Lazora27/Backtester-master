import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_StochasticTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und StochasticTrendStrength
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'StochasticTrendStrength': 1.0
        })
    )
