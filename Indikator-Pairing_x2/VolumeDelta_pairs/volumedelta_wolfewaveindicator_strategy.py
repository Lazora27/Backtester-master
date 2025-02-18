import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeDelta_WolfeWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeDelta und WolfeWaveIndicator
    """
    
    params = (
        ('indicators', {
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            },
            'WolfeWaveIndicator': {
                'class': WolfeWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaveIndicator'>
            }
        }),
        ('weights', {
            'VolumeDelta': 1.0,
            'WolfeWaveIndicator': 1.0
        })
    )
