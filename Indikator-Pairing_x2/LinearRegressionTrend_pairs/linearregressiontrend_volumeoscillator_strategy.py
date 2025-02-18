import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionTrend_VolumeOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionTrend und VolumeOscillator
    """
    
    params = (
        ('indicators', {
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            },
            'VolumeOscillator': {
                'class': VolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeOscillator'>
            }
        }),
        ('weights', {
            'LinearRegressionTrend': 1.0,
            'VolumeOscillator': 1.0
        })
    )
