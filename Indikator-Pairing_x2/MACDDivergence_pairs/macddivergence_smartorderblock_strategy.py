import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_SmartOrderBlock_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und SmartOrderBlock
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'SmartOrderBlock': 1.0
        })
    )
