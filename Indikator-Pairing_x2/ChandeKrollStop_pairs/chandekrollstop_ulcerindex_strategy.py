import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeKrollStop_UlcerIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeKrollStop und UlcerIndex
    """
    
    params = (
        ('indicators', {
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            },
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            }
        }),
        ('weights', {
            'ChandeKrollStop': 1.0,
            'UlcerIndex': 1.0
        })
    )
