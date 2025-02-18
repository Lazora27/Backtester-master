import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OrderBookHeatmap_DemandIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OrderBookHeatmap und DemandIndex
    """
    
    params = (
        ('indicators', {
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            },
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            }
        }),
        ('weights', {
            'OrderBookHeatmap': 1.0,
            'DemandIndex': 1.0
        })
    )
