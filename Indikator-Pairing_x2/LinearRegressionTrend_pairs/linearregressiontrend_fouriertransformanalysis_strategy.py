import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionTrend_FourierTransformAnalysis_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionTrend und FourierTransformAnalysis
    """
    
    params = (
        ('indicators', {
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            },
            'FourierTransformAnalysis': {
                'class': FourierTransformAnalysis,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierTransformAnalysis'>
            }
        }),
        ('weights', {
            'LinearRegressionTrend': 1.0,
            'FourierTransformAnalysis': 1.0
        })
    )
