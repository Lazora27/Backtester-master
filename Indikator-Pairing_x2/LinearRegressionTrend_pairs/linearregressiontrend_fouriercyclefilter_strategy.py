import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionTrend_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionTrend und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'LinearRegressionTrend': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
