import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionTrend_SimpleMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionTrend und SimpleMovingAverage
    """
    
    params = (
        ('indicators', {
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            },
            'SimpleMovingAverage': {
                'class': SimpleMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SimpleMovingAverage'>
            }
        }),
        ('weights', {
            'LinearRegressionTrend': 1.0,
            'SimpleMovingAverage': 1.0
        })
    )
