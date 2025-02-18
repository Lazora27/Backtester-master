import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_RateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und RateOfChange
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'RateOfChange': 1.0
        })
    )
