import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OrderBookHeatmap_ShortTermVolatilityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OrderBookHeatmap und ShortTermVolatilityIndex
    """
    
    params = (
        ('indicators', {
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            },
            'ShortTermVolatilityIndex': {
                'class': ShortTermVolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ShortTermVolatilityIndex'>
            }
        }),
        ('weights', {
            'OrderBookHeatmap': 1.0,
            'ShortTermVolatilityIndex': 1.0
        })
    )
