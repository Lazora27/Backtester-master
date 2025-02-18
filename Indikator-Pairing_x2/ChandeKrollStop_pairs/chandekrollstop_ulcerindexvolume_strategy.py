import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeKrollStop_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeKrollStop und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'ChandeKrollStop': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
