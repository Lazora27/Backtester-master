import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_ChandeKrollStop_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und ChandeKrollStop
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'ChandeKrollStop': 1.0
        })
    )
