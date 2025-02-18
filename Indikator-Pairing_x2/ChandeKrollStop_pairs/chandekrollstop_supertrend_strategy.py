import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeKrollStop_SuperTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeKrollStop und SuperTrend
    """
    
    params = (
        ('indicators', {
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            },
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            }
        }),
        ('weights', {
            'ChandeKrollStop': 1.0,
            'SuperTrend': 1.0
        })
    )
