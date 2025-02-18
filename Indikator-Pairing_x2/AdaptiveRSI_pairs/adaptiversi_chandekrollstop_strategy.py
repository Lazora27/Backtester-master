import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_ChandeKrollStop_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und ChandeKrollStop
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'ChandeKrollStop': 1.0
        })
    )
