import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeKrollStop_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeKrollStop und TimeCycle
    """
    
    params = (
        ('indicators', {
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'ChandeKrollStop': 1.0,
            'TimeCycle': 1.0
        })
    )
