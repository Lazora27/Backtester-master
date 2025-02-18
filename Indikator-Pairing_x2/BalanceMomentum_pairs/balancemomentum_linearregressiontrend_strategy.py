import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_LinearRegressionTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und LinearRegressionTrend
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'LinearRegressionTrend': 1.0
        })
    )
