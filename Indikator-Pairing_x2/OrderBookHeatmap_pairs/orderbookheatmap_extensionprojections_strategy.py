import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OrderBookHeatmap_ExtensionProjections_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OrderBookHeatmap und ExtensionProjections
    """
    
    params = (
        ('indicators', {
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            },
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            }
        }),
        ('weights', {
            'OrderBookHeatmap': 1.0,
            'ExtensionProjections': 1.0
        })
    )
