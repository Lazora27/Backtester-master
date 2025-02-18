import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_LinearRegressionTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und LinearRegressionTrend
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'LinearRegressionTrend': 1.0
        })
    )
