import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_LinearRegressionSlope_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und LinearRegressionSlope
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'LinearRegressionSlope': 1.0
        })
    )
