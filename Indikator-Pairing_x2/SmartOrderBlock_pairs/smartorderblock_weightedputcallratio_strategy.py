import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_WeightedPutCallRatio_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und WeightedPutCallRatio
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'WeightedPutCallRatio': {
                'class': WeightedPutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedPutCallRatio'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'WeightedPutCallRatio': 1.0
        })
    )
