import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_LinearRegressionSlope_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und LinearRegressionSlope
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'LinearRegressionSlope': 1.0
        })
    )
