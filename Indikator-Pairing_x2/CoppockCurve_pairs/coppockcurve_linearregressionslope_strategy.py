import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CoppockCurve_LinearRegressionSlope_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CoppockCurve und LinearRegressionSlope
    """
    
    params = (
        ('indicators', {
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            },
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            }
        }),
        ('weights', {
            'CoppockCurve': 1.0,
            'LinearRegressionSlope': 1.0
        })
    )
