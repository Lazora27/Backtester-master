import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_GannSquareReversal_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und GannSquareReversal
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'GannSquareReversal': 1.0
        })
    )
