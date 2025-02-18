import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_StochasticTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und StochasticTrendStrength
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'StochasticTrendStrength': 1.0
        })
    )
