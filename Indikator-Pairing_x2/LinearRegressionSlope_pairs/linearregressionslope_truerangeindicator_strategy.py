import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionSlope_TrueRangeIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionSlope und TrueRangeIndicator
    """
    
    params = (
        ('indicators', {
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            },
            'TrueRangeIndicator': {
                'class': TrueRangeIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRangeIndicator'>
            }
        }),
        ('weights', {
            'LinearRegressionSlope': 1.0,
            'TrueRangeIndicator': 1.0
        })
    )
