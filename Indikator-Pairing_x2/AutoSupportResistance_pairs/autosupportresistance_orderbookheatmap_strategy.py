import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_OrderBookHeatmap_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und OrderBookHeatmap
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'OrderBookHeatmap': 1.0
        })
    )
