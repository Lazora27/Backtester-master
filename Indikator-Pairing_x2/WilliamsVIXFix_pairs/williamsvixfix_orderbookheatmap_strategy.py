import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsVIXFix_OrderBookHeatmap_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsVIXFix und OrderBookHeatmap
    """
    
    params = (
        ('indicators', {
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            },
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            }
        }),
        ('weights', {
            'WilliamsVIXFix': 1.0,
            'OrderBookHeatmap': 1.0
        })
    )
