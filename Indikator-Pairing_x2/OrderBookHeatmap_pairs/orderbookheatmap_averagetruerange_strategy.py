import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OrderBookHeatmap_AverageTrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OrderBookHeatmap und AverageTrueRange
    """
    
    params = (
        ('indicators', {
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            },
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            }
        }),
        ('weights', {
            'OrderBookHeatmap': 1.0,
            'AverageTrueRange': 1.0
        })
    )
