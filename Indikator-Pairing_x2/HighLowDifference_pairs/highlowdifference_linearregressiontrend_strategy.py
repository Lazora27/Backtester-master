import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_LinearRegressionTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und LinearRegressionTrend
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'LinearRegressionTrend': 1.0
        })
    )
