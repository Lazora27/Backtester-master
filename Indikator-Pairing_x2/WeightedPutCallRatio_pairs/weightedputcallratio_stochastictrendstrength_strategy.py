import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedPutCallRatio_StochasticTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedPutCallRatio und StochasticTrendStrength
    """
    
    params = (
        ('indicators', {
            'WeightedPutCallRatio': {
                'class': WeightedPutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedPutCallRatio'>
            },
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            }
        }),
        ('weights', {
            'WeightedPutCallRatio': 1.0,
            'StochasticTrendStrength': 1.0
        })
    )
