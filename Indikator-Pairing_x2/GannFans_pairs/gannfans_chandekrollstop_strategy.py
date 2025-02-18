import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannFans_ChandeKrollStop_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannFans und ChandeKrollStop
    """
    
    params = (
        ('indicators', {
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            },
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            }
        }),
        ('weights', {
            'GannFans': 1.0,
            'ChandeKrollStop': 1.0
        })
    )
