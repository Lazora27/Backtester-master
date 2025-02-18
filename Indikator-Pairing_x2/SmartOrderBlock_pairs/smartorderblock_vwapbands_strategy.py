import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_VWAPBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und VWAPBands
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'VWAPBands': 1.0
        })
    )
