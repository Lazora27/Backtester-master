import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionTrend_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionTrend und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'LinearRegressionTrend': 1.0,
            'AverageLogRange': 1.0
        })
    )
