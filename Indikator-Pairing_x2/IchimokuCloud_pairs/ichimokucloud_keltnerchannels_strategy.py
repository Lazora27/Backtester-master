import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IchimokuCloud_KeltnerChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IchimokuCloud und KeltnerChannels
    """
    
    params = (
        ('indicators', {
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            },
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            }
        }),
        ('weights', {
            'IchimokuCloud': 1.0,
            'KeltnerChannels': 1.0
        })
    )
