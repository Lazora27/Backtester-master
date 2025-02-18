import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvanceDeclineLine_LinearRegressionSlope_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvanceDeclineLine und LinearRegressionSlope
    """
    
    params = (
        ('indicators', {
            'AdvanceDeclineLine': {
                'class': AdvanceDeclineLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvanceDeclineLine'>
            },
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            }
        }),
        ('weights', {
            'AdvanceDeclineLine': 1.0,
            'LinearRegressionSlope': 1.0
        })
    )
