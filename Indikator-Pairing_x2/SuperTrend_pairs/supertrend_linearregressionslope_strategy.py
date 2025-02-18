import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperTrend_LinearRegressionSlope_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperTrend und LinearRegressionSlope
    """
    
    params = (
        ('indicators', {
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            },
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            }
        }),
        ('weights', {
            'SuperTrend': 1.0,
            'LinearRegressionSlope': 1.0
        })
    )
