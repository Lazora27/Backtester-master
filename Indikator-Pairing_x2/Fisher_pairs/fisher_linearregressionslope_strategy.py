import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_LinearRegressionSlope_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und LinearRegressionSlope
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'LinearRegressionSlope': 1.0
        })
    )
