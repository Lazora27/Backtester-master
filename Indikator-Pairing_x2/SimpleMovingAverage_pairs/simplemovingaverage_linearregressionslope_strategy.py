import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SimpleMovingAverage_LinearRegressionSlope_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SimpleMovingAverage und LinearRegressionSlope
    """
    
    params = (
        ('indicators', {
            'SimpleMovingAverage': {
                'class': SimpleMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SimpleMovingAverage'>
            },
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            }
        }),
        ('weights', {
            'SimpleMovingAverage': 1.0,
            'LinearRegressionSlope': 1.0
        })
    )
