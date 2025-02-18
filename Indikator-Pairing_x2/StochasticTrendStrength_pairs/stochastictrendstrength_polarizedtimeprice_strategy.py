import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
