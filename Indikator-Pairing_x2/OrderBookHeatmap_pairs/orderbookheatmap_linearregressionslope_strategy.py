import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OrderBookHeatmap_LinearRegressionSlope_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OrderBookHeatmap und LinearRegressionSlope
    """
    
    params = (
        ('indicators', {
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            },
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            }
        }),
        ('weights', {
            'OrderBookHeatmap': 1.0,
            'LinearRegressionSlope': 1.0
        })
    )
