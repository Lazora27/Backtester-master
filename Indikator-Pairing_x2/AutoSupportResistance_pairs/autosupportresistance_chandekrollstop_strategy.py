import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_ChandeKrollStop_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und ChandeKrollStop
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'ChandeKrollStop': 1.0
        })
    )
