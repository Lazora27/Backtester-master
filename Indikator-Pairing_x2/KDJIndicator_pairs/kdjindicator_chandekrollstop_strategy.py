import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KDJIndicator_ChandeKrollStop_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KDJIndicator und ChandeKrollStop
    """
    
    params = (
        ('indicators', {
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            },
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            }
        }),
        ('weights', {
            'KDJIndicator': 1.0,
            'ChandeKrollStop': 1.0
        })
    )
