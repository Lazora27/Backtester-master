import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeKrollStop_TrueRangeIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeKrollStop und TrueRangeIndicator
    """
    
    params = (
        ('indicators', {
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            },
            'TrueRangeIndicator': {
                'class': TrueRangeIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRangeIndicator'>
            }
        }),
        ('weights', {
            'ChandeKrollStop': 1.0,
            'TrueRangeIndicator': 1.0
        })
    )
