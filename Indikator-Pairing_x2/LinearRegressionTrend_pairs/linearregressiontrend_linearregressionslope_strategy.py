import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionTrend_LinearRegressionSlope_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionTrend und LinearRegressionSlope
    """
    
    params = (
        ('indicators', {
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            },
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            }
        }),
        ('weights', {
            'LinearRegressionTrend': 1.0,
            'LinearRegressionSlope': 1.0
        })
    )
