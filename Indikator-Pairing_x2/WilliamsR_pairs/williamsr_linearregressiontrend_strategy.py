import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_LinearRegressionTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und LinearRegressionTrend
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'LinearRegressionTrend': 1.0
        })
    )
