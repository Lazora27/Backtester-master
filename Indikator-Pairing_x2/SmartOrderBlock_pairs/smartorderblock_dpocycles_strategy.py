import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und DPOCycles
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'DPOCycles': 1.0
        })
    )
