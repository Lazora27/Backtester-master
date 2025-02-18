import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_AroonIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und AroonIndicator
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'AroonIndicator': {
                'class': AroonIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AroonIndicator'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'AroonIndicator': 1.0
        })
    )
