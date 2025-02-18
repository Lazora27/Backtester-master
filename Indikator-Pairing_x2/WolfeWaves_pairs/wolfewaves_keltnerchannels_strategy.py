import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaves_KeltnerChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaves und KeltnerChannels
    """
    
    params = (
        ('indicators', {
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            },
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            }
        }),
        ('weights', {
            'WolfeWaves': 1.0,
            'KeltnerChannels': 1.0
        })
    )
