import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'HilbertTrendline': 1.0
        })
    )
