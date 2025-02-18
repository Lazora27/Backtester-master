import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_StochasticTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und StochasticTrendStrength
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'StochasticTrendStrength': 1.0
        })
    )
