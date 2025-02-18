import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'EhlersDecycler': 1.0
        })
    )
