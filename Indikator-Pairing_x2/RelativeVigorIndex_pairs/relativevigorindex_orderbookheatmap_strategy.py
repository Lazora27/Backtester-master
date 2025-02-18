import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeVigorIndex_OrderBookHeatmap_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeVigorIndex und OrderBookHeatmap
    """
    
    params = (
        ('indicators', {
            'RelativeVigorIndex': {
                'class': RelativeVigorIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVigorIndex'>
            },
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            }
        }),
        ('weights', {
            'RelativeVigorIndex': 1.0,
            'OrderBookHeatmap': 1.0
        })
    )
