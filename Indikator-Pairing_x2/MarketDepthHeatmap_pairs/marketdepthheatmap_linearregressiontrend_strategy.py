import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketDepthHeatmap_LinearRegressionTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketDepthHeatmap und LinearRegressionTrend
    """
    
    params = (
        ('indicators', {
            'MarketDepthHeatmap': {
                'class': MarketDepthHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketDepthHeatmap'>
            },
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            }
        }),
        ('weights', {
            'MarketDepthHeatmap': 1.0,
            'LinearRegressionTrend': 1.0
        })
    )
