import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OrderBookHeatmap_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OrderBookHeatmap und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'OrderBookHeatmap': 1.0,
            'BradleySiderograph': 1.0
        })
    )
