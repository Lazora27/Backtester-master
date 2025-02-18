import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_OrderBookHeatmap_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und OrderBookHeatmap
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'OrderBookHeatmap': 1.0
        })
    )
