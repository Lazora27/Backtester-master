import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionTrend_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionTrend und OpenInterest
    """
    
    params = (
        ('indicators', {
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'LinearRegressionTrend': 1.0,
            'OpenInterest': 1.0
        })
    )
