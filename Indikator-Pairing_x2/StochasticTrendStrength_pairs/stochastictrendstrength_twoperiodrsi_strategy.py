import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_TwoPeriodRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und TwoPeriodRSI
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'TwoPeriodRSI': 1.0
        })
    )
