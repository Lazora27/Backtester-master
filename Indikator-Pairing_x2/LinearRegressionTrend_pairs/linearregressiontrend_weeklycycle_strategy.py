import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionTrend_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionTrend und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'LinearRegressionTrend': 1.0,
            'WeeklyCycle': 1.0
        })
    )
