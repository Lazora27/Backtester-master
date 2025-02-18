import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_GannFans_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und GannFans
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'GannFans': 1.0
        })
    )
