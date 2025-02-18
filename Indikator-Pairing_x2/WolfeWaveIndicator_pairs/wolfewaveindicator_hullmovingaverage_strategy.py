import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaveIndicator_HullMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaveIndicator und HullMovingAverage
    """
    
    params = (
        ('indicators', {
            'WolfeWaveIndicator': {
                'class': WolfeWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaveIndicator'>
            },
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            }
        }),
        ('weights', {
            'WolfeWaveIndicator': 1.0,
            'HullMovingAverage': 1.0
        })
    )
