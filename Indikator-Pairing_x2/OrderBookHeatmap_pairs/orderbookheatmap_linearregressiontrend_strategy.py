import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OrderBookHeatmap_LinearRegressionTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OrderBookHeatmap und LinearRegressionTrend
    """
    
    params = (
        ('indicators', {
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            },
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            }
        }),
        ('weights', {
            'OrderBookHeatmap': 1.0,
            'LinearRegressionTrend': 1.0
        })
    )
