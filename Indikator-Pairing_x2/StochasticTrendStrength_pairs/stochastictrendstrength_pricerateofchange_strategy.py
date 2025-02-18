import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_PriceRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und PriceRateOfChange
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'PriceRateOfChange': 1.0
        })
    )
