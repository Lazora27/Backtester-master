import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannAngles_KeltnerChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannAngles und KeltnerChannels
    """
    
    params = (
        ('indicators', {
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            },
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            }
        }),
        ('weights', {
            'GannAngles': 1.0,
            'KeltnerChannels': 1.0
        })
    )
