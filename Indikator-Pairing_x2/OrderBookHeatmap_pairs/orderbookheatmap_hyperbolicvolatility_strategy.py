import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OrderBookHeatmap_HyperbolicVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OrderBookHeatmap und HyperbolicVolatility
    """
    
    params = (
        ('indicators', {
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            },
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            }
        }),
        ('weights', {
            'OrderBookHeatmap': 1.0,
            'HyperbolicVolatility': 1.0
        })
    )
