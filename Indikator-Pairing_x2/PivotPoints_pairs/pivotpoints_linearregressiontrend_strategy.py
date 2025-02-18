import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PivotPoints_LinearRegressionTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PivotPoints und LinearRegressionTrend
    """
    
    params = (
        ('indicators', {
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            },
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            }
        }),
        ('weights', {
            'PivotPoints': 1.0,
            'LinearRegressionTrend': 1.0
        })
    )
