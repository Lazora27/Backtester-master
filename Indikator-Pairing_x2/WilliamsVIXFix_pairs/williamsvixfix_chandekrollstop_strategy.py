import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsVIXFix_ChandeKrollStop_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsVIXFix und ChandeKrollStop
    """
    
    params = (
        ('indicators', {
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            },
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            }
        }),
        ('weights', {
            'WilliamsVIXFix': 1.0,
            'ChandeKrollStop': 1.0
        })
    )
