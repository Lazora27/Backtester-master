import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketDepthHeatmap_LinearRegressionSlope_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketDepthHeatmap und LinearRegressionSlope
    """
    
    params = (
        ('indicators', {
            'MarketDepthHeatmap': {
                'class': MarketDepthHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketDepthHeatmap'>
            },
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            }
        }),
        ('weights', {
            'MarketDepthHeatmap': 1.0,
            'LinearRegressionSlope': 1.0
        })
    )
