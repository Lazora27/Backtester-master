import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_PriceDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und PriceDelta
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'PriceDelta': 1.0
        })
    )
