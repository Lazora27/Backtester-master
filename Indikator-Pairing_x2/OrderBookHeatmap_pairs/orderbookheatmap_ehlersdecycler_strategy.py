import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OrderBookHeatmap_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OrderBookHeatmap und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'OrderBookHeatmap': 1.0,
            'EhlersDecycler': 1.0
        })
    )
