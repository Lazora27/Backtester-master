import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionSlope_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionSlope und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'LinearRegressionSlope': 1.0,
            'WeeklyCycle': 1.0
        })
    )
