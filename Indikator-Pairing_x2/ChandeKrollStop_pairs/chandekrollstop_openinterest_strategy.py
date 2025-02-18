import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeKrollStop_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeKrollStop und OpenInterest
    """
    
    params = (
        ('indicators', {
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'ChandeKrollStop': 1.0,
            'OpenInterest': 1.0
        })
    )
