import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
