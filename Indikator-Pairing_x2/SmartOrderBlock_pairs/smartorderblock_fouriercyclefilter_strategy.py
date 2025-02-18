import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
