import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_KeltnerChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und KeltnerChannels
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'KeltnerChannels': 1.0
        })
    )
