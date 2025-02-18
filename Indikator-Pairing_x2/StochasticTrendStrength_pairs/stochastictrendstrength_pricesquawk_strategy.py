import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_PriceSquawk_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und PriceSquawk
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'PriceSquawk': 1.0
        })
    )
