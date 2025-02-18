import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_GannSquares_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und GannSquares
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'GannSquares': 1.0
        })
    )
