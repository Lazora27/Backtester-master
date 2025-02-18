import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaves_DonchianChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaves und DonchianChannels
    """
    
    params = (
        ('indicators', {
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            },
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            }
        }),
        ('weights', {
            'WolfeWaves': 1.0,
            'DonchianChannels': 1.0
        })
    )
