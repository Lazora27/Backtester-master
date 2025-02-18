import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OrderBookHeatmap_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OrderBookHeatmap und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'OrderBookHeatmap': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
