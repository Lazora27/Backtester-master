import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_ChandeKrollStop_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und ChandeKrollStop
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'ChandeKrollStop': 1.0
        })
    )
