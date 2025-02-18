import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionSlope_TRIXIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionSlope und TRIXIndicator
    """
    
    params = (
        ('indicators', {
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            },
            'TRIXIndicator': {
                'class': TRIXIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TRIXIndicator'>
            }
        }),
        ('weights', {
            'LinearRegressionSlope': 1.0,
            'TRIXIndicator': 1.0
        })
    )
