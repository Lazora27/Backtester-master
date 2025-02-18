import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_LinearRegressionSlope_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und LinearRegressionSlope
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'LinearRegressionSlope': 1.0
        })
    )
