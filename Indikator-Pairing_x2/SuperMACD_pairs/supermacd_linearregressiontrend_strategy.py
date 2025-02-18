import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_LinearRegressionTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und LinearRegressionTrend
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'LinearRegressionTrend': 1.0
        })
    )
