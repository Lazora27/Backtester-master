import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeDelta_ChandeKrollStop_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeDelta und ChandeKrollStop
    """
    
    params = (
        ('indicators', {
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            },
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            }
        }),
        ('weights', {
            'VolumeDelta': 1.0,
            'ChandeKrollStop': 1.0
        })
    )
