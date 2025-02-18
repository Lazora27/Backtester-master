import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_StochasticTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und StochasticTrendStrength
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'StochasticTrendStrength': 1.0
        })
    )
