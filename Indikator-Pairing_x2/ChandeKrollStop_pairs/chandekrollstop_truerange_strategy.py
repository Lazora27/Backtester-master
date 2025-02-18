import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeKrollStop_TrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeKrollStop und TrueRange
    """
    
    params = (
        ('indicators', {
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            },
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            }
        }),
        ('weights', {
            'ChandeKrollStop': 1.0,
            'TrueRange': 1.0
        })
    )
