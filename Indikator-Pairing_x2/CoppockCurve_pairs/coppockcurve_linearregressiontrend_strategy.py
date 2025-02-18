import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CoppockCurve_LinearRegressionTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CoppockCurve und LinearRegressionTrend
    """
    
    params = (
        ('indicators', {
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            },
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            }
        }),
        ('weights', {
            'CoppockCurve': 1.0,
            'LinearRegressionTrend': 1.0
        })
    )
