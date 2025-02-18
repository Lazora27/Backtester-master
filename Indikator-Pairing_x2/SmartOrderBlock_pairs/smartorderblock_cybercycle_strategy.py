import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und CyberCycle
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'CyberCycle': 1.0
        })
    )
