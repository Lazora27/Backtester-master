import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_TickVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und TickVolume
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'TickVolume': 1.0
        })
    )
