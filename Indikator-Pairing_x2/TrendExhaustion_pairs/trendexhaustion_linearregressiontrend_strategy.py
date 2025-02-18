import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_LinearRegressionTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und LinearRegressionTrend
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'LinearRegressionTrend': 1.0
        })
    )
