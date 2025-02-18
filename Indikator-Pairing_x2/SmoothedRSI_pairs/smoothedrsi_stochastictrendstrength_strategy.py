import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_StochasticTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und StochasticTrendStrength
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'StochasticTrendStrength': 1.0
        })
    )
