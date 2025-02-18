import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionTrend_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionTrend und TrendCycles
    """
    
    params = (
        ('indicators', {
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'LinearRegressionTrend': 1.0,
            'TrendCycles': 1.0
        })
    )
