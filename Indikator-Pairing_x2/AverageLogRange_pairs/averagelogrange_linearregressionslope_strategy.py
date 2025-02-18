import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageLogRange_LinearRegressionSlope_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageLogRange und LinearRegressionSlope
    """
    
    params = (
        ('indicators', {
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            },
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            }
        }),
        ('weights', {
            'AverageLogRange': 1.0,
            'LinearRegressionSlope': 1.0
        })
    )
