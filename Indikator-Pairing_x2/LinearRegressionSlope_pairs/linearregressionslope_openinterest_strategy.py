import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionSlope_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionSlope und OpenInterest
    """
    
    params = (
        ('indicators', {
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'LinearRegressionSlope': 1.0,
            'OpenInterest': 1.0
        })
    )
