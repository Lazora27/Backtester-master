import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionSlope_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionSlope und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'LinearRegressionSlope': 1.0,
            'HilbertTrendline': 1.0
        })
    )
