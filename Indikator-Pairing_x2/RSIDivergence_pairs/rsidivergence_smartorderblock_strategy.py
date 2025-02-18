import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_SmartOrderBlock_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und SmartOrderBlock
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'SmartOrderBlock': 1.0
        })
    )
