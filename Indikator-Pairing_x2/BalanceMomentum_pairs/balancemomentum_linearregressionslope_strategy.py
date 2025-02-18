import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_LinearRegressionSlope_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und LinearRegressionSlope
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'LinearRegressionSlope': 1.0
        })
    )
