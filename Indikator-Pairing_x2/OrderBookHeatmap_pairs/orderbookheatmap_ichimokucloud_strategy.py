import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OrderBookHeatmap_IchimokuCloud_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OrderBookHeatmap und IchimokuCloud
    """
    
    params = (
        ('indicators', {
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            },
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            }
        }),
        ('weights', {
            'OrderBookHeatmap': 1.0,
            'IchimokuCloud': 1.0
        })
    )
