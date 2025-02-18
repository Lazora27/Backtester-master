import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_AdaptiveATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und AdaptiveATR
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'AdaptiveATR': 1.0
        })
    )
