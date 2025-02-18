import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'AccelerationBands': 1.0
        })
    )
