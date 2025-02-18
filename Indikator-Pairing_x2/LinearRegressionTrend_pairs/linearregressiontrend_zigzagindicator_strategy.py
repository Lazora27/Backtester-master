import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionTrend_ZigZagIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionTrend und ZigZagIndicator
    """
    
    params = (
        ('indicators', {
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            },
            'ZigZagIndicator': {
                'class': ZigZagIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZigZagIndicator'>
            }
        }),
        ('weights', {
            'LinearRegressionTrend': 1.0,
            'ZigZagIndicator': 1.0
        })
    )
