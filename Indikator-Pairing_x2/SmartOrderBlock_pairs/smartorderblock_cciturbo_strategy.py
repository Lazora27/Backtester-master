import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und CCITurbo
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'CCITurbo': 1.0
        })
    )
