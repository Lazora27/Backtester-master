import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_FisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und FisherTransform
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'FisherTransform': 1.0
        })
    )
