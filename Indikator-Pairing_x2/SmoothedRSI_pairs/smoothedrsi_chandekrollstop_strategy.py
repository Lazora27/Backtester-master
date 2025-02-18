import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_ChandeKrollStop_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und ChandeKrollStop
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'ChandeKrollStop': 1.0
        })
    )
