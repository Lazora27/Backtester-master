import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_OrderBookHeatmap_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und OrderBookHeatmap
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'OrderBookHeatmap': 1.0
        })
    )
