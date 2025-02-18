import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_CVIRatio_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und CVIRatio
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'CVIRatio': 1.0
        })
    )
