import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanSummationIndex_OrderBookHeatmap_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanSummationIndex und OrderBookHeatmap
    """
    
    params = (
        ('indicators', {
            'McClellanSummationIndex': {
                'class': McClellanSummationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanSummationIndex'>
            },
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            }
        }),
        ('weights', {
            'McClellanSummationIndex': 1.0,
            'OrderBookHeatmap': 1.0
        })
    )
