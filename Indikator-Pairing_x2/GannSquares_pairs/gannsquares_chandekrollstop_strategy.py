import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquares_ChandeKrollStop_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquares und ChandeKrollStop
    """
    
    params = (
        ('indicators', {
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            },
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            }
        }),
        ('weights', {
            'GannSquares': 1.0,
            'ChandeKrollStop': 1.0
        })
    )
