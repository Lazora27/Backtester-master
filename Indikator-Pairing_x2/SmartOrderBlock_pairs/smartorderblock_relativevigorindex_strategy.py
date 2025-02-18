import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_RelativeVigorIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und RelativeVigorIndex
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'RelativeVigorIndex': {
                'class': RelativeVigorIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVigorIndex'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'RelativeVigorIndex': 1.0
        })
    )
