import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeKrollStop_IchimokuCloud_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeKrollStop und IchimokuCloud
    """
    
    params = (
        ('indicators', {
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            },
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            }
        }),
        ('weights', {
            'ChandeKrollStop': 1.0,
            'IchimokuCloud': 1.0
        })
    )
