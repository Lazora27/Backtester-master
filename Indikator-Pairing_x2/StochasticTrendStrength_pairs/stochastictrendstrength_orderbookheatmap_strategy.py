import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_OrderBookHeatmap_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und OrderBookHeatmap
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'OrderBookHeatmap': 1.0
        })
    )
