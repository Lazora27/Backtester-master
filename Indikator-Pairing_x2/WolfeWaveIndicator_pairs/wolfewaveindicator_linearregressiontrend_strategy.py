import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaveIndicator_LinearRegressionTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaveIndicator und LinearRegressionTrend
    """
    
    params = (
        ('indicators', {
            'WolfeWaveIndicator': {
                'class': WolfeWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaveIndicator'>
            },
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            }
        }),
        ('weights', {
            'WolfeWaveIndicator': 1.0,
            'LinearRegressionTrend': 1.0
        })
    )
