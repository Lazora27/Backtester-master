import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionTrend_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionTrend und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'LinearRegressionTrend': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
