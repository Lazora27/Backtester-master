import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionTrend_MomentumTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionTrend und MomentumTrendStrength
    """
    
    params = (
        ('indicators', {
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            },
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            }
        }),
        ('weights', {
            'LinearRegressionTrend': 1.0,
            'MomentumTrendStrength': 1.0
        })
    )
