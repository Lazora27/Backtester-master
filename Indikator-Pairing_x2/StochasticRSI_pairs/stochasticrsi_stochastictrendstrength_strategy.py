import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_StochasticTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und StochasticTrendStrength
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'StochasticTrendStrength': 1.0
        })
    )
