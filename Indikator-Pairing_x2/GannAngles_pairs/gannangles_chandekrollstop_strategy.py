import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannAngles_ChandeKrollStop_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannAngles und ChandeKrollStop
    """
    
    params = (
        ('indicators', {
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            },
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            }
        }),
        ('weights', {
            'GannAngles': 1.0,
            'ChandeKrollStop': 1.0
        })
    )
