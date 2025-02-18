import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_ChandeKrollStop_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und ChandeKrollStop
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'ChandeKrollStop': 1.0
        })
    )
