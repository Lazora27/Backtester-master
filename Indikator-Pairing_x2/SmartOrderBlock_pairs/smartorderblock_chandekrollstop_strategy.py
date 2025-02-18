import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_ChandeKrollStop_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und ChandeKrollStop
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'ChandeKrollStop': 1.0
        })
    )
