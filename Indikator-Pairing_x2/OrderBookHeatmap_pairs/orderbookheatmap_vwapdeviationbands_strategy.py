import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OrderBookHeatmap_VWAPDeviationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OrderBookHeatmap und VWAPDeviationBands
    """
    
    params = (
        ('indicators', {
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            },
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            }
        }),
        ('weights', {
            'OrderBookHeatmap': 1.0,
            'VWAPDeviationBands': 1.0
        })
    )
