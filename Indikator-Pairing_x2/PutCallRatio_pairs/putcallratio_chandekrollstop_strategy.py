import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_ChandeKrollStop_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und ChandeKrollStop
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'ChandeKrollStop': 1.0
        })
    )
