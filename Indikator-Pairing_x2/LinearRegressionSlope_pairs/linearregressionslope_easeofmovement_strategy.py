import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionSlope_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionSlope und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'LinearRegressionSlope': 1.0,
            'EaseOfMovement': 1.0
        })
    )
