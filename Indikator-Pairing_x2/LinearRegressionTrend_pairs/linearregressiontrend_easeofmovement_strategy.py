import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionTrend_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionTrend und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'LinearRegressionTrend': 1.0,
            'EaseOfMovement': 1.0
        })
    )
