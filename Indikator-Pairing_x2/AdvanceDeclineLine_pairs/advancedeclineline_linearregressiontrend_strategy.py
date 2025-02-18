import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvanceDeclineLine_LinearRegressionTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvanceDeclineLine und LinearRegressionTrend
    """
    
    params = (
        ('indicators', {
            'AdvanceDeclineLine': {
                'class': AdvanceDeclineLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvanceDeclineLine'>
            },
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            }
        }),
        ('weights', {
            'AdvanceDeclineLine': 1.0,
            'LinearRegressionTrend': 1.0
        })
    )
