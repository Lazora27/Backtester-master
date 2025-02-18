import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeKrollStop_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeKrollStop und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'ChandeKrollStop': 1.0,
            'SmoothedCycle': 1.0
        })
    )
