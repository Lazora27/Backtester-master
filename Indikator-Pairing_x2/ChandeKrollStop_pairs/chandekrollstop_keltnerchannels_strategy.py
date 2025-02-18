import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeKrollStop_KeltnerChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeKrollStop und KeltnerChannels
    """
    
    params = (
        ('indicators', {
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            },
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            }
        }),
        ('weights', {
            'ChandeKrollStop': 1.0,
            'KeltnerChannels': 1.0
        })
    )
