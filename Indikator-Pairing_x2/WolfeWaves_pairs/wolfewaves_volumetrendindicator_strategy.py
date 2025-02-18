import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaves_VolumeTrendIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaves und VolumeTrendIndicator
    """
    
    params = (
        ('indicators', {
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            },
            'VolumeTrendIndicator': {
                'class': VolumeTrendIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeTrendIndicator'>
            }
        }),
        ('weights', {
            'WolfeWaves': 1.0,
            'VolumeTrendIndicator': 1.0
        })
    )
