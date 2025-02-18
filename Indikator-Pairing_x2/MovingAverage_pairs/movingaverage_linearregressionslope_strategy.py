import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MovingAverage_LinearRegressionSlope_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MovingAverage und LinearRegressionSlope
    """
    
    params = (
        ('indicators', {
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            },
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            }
        }),
        ('weights', {
            'MovingAverage': 1.0,
            'LinearRegressionSlope': 1.0
        })
    )
