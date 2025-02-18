import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OrderBookHeatmap_CenterOfGravity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OrderBookHeatmap und CenterOfGravity
    """
    
    params = (
        ('indicators', {
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            },
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            }
        }),
        ('weights', {
            'OrderBookHeatmap': 1.0,
            'CenterOfGravity': 1.0
        })
    )
