import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_MomentumTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und MomentumTrendStrength
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'MomentumTrendStrength': 1.0
        })
    )
