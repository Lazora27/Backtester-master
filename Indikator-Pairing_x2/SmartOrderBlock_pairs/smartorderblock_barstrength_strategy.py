import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und BarStrength
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'BarStrength': 1.0
        })
    )
