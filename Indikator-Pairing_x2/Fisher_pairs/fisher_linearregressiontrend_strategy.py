import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_LinearRegressionTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und LinearRegressionTrend
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'LinearRegressionTrend': 1.0
        })
    )
