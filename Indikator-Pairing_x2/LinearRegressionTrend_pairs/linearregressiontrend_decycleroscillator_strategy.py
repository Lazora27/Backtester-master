import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionTrend_DecyclerOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionTrend und DecyclerOscillator
    """
    
    params = (
        ('indicators', {
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            },
            'DecyclerOscillator': {
                'class': DecyclerOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DecyclerOscillator'>
            }
        }),
        ('weights', {
            'LinearRegressionTrend': 1.0,
            'DecyclerOscillator': 1.0
        })
    )
