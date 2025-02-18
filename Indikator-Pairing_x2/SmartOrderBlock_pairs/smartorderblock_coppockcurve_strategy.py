import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_CoppockCurve_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und CoppockCurve
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'CoppockCurve': 1.0
        })
    )
