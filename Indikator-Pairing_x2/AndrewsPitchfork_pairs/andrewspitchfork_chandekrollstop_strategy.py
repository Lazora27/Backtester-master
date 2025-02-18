import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AndrewsPitchfork_ChandeKrollStop_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AndrewsPitchfork und ChandeKrollStop
    """
    
    params = (
        ('indicators', {
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            },
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            }
        }),
        ('weights', {
            'AndrewsPitchfork': 1.0,
            'ChandeKrollStop': 1.0
        })
    )
