import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionTrend_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionTrend und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'LinearRegressionTrend': 1.0,
            'SmoothedCycle': 1.0
        })
    )
