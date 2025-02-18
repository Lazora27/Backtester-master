import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoFibonacci_LinearRegressionTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoFibonacci und LinearRegressionTrend
    """
    
    params = (
        ('indicators', {
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            },
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            }
        }),
        ('weights', {
            'AutoFibonacci': 1.0,
            'LinearRegressionTrend': 1.0
        })
    )
