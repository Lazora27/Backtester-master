import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HullMovingAverage_LinearRegressionSlope_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HullMovingAverage und LinearRegressionSlope
    """
    
    params = (
        ('indicators', {
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            },
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            }
        }),
        ('weights', {
            'HullMovingAverage': 1.0,
            'LinearRegressionSlope': 1.0
        })
    )
