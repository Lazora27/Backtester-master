import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionTrend_AdaptiveATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionTrend und AdaptiveATR
    """
    
    params = (
        ('indicators', {
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            },
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            }
        }),
        ('weights', {
            'LinearRegressionTrend': 1.0,
            'AdaptiveATR': 1.0
        })
    )
