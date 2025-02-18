import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OrderBookHeatmap_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OrderBookHeatmap und TrendCycles
    """
    
    params = (
        ('indicators', {
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'OrderBookHeatmap': 1.0,
            'TrendCycles': 1.0
        })
    )
