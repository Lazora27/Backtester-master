import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaveIndicator_VolumeTrendIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaveIndicator und VolumeTrendIndicator
    """
    
    params = (
        ('indicators', {
            'WolfeWaveIndicator': {
                'class': WolfeWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaveIndicator'>
            },
            'VolumeTrendIndicator': {
                'class': VolumeTrendIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeTrendIndicator'>
            }
        }),
        ('weights', {
            'WolfeWaveIndicator': 1.0,
            'VolumeTrendIndicator': 1.0
        })
    )
