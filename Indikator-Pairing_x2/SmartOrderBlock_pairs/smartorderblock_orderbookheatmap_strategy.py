import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_OrderBookHeatmap_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und OrderBookHeatmap
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'OrderBookHeatmap': 1.0
        })
    )
