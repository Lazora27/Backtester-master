import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OrderBookHeatmap_VolatilityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OrderBookHeatmap und VolatilityIndex
    """
    
    params = (
        ('indicators', {
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            },
            'VolatilityIndex': {
                'class': VolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolatilityIndex'>
            }
        }),
        ('weights', {
            'OrderBookHeatmap': 1.0,
            'VolatilityIndex': 1.0
        })
    )
