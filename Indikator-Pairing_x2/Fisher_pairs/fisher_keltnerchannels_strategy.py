import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_KeltnerChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und KeltnerChannels
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'KeltnerChannels': 1.0
        })
    )
