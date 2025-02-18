import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeProfile_ChandeKrollStop_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeProfile und ChandeKrollStop
    """
    
    params = (
        ('indicators', {
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            },
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            }
        }),
        ('weights', {
            'VolumeProfile': 1.0,
            'ChandeKrollStop': 1.0
        })
    )
