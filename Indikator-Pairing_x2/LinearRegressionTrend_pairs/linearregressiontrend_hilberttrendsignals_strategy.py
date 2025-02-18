import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionTrend_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionTrend und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'LinearRegressionTrend': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
