import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquareReversal_ChandeKrollStop_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquareReversal und ChandeKrollStop
    """
    
    params = (
        ('indicators', {
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            },
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            }
        }),
        ('weights', {
            'GannSquareReversal': 1.0,
            'ChandeKrollStop': 1.0
        })
    )
