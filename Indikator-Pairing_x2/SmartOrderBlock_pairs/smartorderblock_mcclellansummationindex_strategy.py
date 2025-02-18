import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_McClellanSummationIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und McClellanSummationIndex
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'McClellanSummationIndex': {
                'class': McClellanSummationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanSummationIndex'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'McClellanSummationIndex': 1.0
        })
    )
