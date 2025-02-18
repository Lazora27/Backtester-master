import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveTrendLine_ChandeKrollStop_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveTrendLine und ChandeKrollStop
    """
    
    params = (
        ('indicators', {
            'AdaptiveTrendLine': {
                'class': AdaptiveTrendLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveTrendLine'>
            },
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            }
        }),
        ('weights', {
            'AdaptiveTrendLine': 1.0,
            'ChandeKrollStop': 1.0
        })
    )
