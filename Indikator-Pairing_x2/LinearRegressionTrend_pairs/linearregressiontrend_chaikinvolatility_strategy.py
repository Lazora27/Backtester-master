import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionTrend_ChaikinVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionTrend und ChaikinVolatility
    """
    
    params = (
        ('indicators', {
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            },
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            }
        }),
        ('weights', {
            'LinearRegressionTrend': 1.0,
            'ChaikinVolatility': 1.0
        })
    )
