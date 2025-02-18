import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
