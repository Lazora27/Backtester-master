import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'AverageLogRange': 1.0
        })
    )
