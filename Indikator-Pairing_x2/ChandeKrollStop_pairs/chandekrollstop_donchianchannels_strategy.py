import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeKrollStop_DonchianChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeKrollStop und DonchianChannels
    """
    
    params = (
        ('indicators', {
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            },
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            }
        }),
        ('weights', {
            'ChandeKrollStop': 1.0,
            'DonchianChannels': 1.0
        })
    )
