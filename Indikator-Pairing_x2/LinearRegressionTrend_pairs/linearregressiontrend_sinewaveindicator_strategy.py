import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionTrend_SineWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionTrend und SineWaveIndicator
    """
    
    params = (
        ('indicators', {
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            },
            'SineWaveIndicator': {
                'class': SineWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveIndicator'>
            }
        }),
        ('weights', {
            'LinearRegressionTrend': 1.0,
            'SineWaveIndicator': 1.0
        })
    )
