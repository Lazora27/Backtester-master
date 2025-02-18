import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeKrollStop_AdaptiveATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeKrollStop und AdaptiveATR
    """
    
    params = (
        ('indicators', {
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            },
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            }
        }),
        ('weights', {
            'ChandeKrollStop': 1.0,
            'AdaptiveATR': 1.0
        })
    )
