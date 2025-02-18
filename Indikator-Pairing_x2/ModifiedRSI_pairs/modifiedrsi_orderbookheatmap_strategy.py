import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_OrderBookHeatmap_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und OrderBookHeatmap
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'OrderBookHeatmap': 1.0
        })
    )
