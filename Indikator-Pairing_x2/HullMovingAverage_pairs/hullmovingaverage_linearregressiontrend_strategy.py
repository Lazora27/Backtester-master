import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HullMovingAverage_LinearRegressionTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HullMovingAverage und LinearRegressionTrend
    """
    
    params = (
        ('indicators', {
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            },
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            }
        }),
        ('weights', {
            'HullMovingAverage': 1.0,
            'LinearRegressionTrend': 1.0
        })
    )
