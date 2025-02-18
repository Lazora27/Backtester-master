import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OrderBookHeatmap_GannFans_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OrderBookHeatmap und GannFans
    """
    
    params = (
        ('indicators', {
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            },
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            }
        }),
        ('weights', {
            'OrderBookHeatmap': 1.0,
            'GannFans': 1.0
        })
    )
