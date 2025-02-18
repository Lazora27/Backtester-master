import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeKrollStop_HeikenAshiTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeKrollStop und HeikenAshiTrend
    """
    
    params = (
        ('indicators', {
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            },
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            }
        }),
        ('weights', {
            'ChandeKrollStop': 1.0,
            'HeikenAshiTrend': 1.0
        })
    )
