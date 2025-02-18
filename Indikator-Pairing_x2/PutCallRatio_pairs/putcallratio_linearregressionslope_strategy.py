import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_LinearRegressionSlope_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und LinearRegressionSlope
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'LinearRegressionSlope': 1.0
        })
    )
