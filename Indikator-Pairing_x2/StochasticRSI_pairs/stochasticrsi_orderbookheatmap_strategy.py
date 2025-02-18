import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_OrderBookHeatmap_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und OrderBookHeatmap
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'OrderBookHeatmap': 1.0
        })
    )
