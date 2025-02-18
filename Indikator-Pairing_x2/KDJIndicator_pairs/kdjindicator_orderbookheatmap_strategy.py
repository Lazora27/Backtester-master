import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KDJIndicator_OrderBookHeatmap_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KDJIndicator und OrderBookHeatmap
    """
    
    params = (
        ('indicators', {
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            },
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            }
        }),
        ('weights', {
            'KDJIndicator': 1.0,
            'OrderBookHeatmap': 1.0
        })
    )
