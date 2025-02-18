import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_LinearRegressionSlope_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und LinearRegressionSlope
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'LinearRegressionSlope': 1.0
        })
    )
