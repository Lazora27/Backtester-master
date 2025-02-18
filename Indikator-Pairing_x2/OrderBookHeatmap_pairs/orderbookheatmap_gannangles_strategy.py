import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OrderBookHeatmap_GannAngles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OrderBookHeatmap und GannAngles
    """
    
    params = (
        ('indicators', {
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            },
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            }
        }),
        ('weights', {
            'OrderBookHeatmap': 1.0,
            'GannAngles': 1.0
        })
    )
