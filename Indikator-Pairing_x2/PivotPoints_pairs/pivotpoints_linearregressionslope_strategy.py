import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PivotPoints_LinearRegressionSlope_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PivotPoints und LinearRegressionSlope
    """
    
    params = (
        ('indicators', {
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            },
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            }
        }),
        ('weights', {
            'PivotPoints': 1.0,
            'LinearRegressionSlope': 1.0
        })
    )
