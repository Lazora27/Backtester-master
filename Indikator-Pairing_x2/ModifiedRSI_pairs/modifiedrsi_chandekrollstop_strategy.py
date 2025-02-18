import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_ChandeKrollStop_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und ChandeKrollStop
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'ChandeKrollStop': 1.0
        })
    )
