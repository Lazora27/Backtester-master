import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OrderBookHeatmap_ParabolicSAR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OrderBookHeatmap und ParabolicSAR
    """
    
    params = (
        ('indicators', {
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            },
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            }
        }),
        ('weights', {
            'OrderBookHeatmap': 1.0,
            'ParabolicSAR': 1.0
        })
    )
