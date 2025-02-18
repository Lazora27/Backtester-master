import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OrderBookHeatmap_ChandeKrollStop_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OrderBookHeatmap und ChandeKrollStop
    """
    
    params = (
        ('indicators', {
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            },
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            }
        }),
        ('weights', {
            'OrderBookHeatmap': 1.0,
            'ChandeKrollStop': 1.0
        })
    )
