import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionTrend_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionTrend und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'LinearRegressionTrend': 1.0,
            'AccelerationBands': 1.0
        })
    )
