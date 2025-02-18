import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_PriceCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und PriceCycleOscillator
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'PriceCycleOscillator': {
                'class': PriceCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceCycleOscillator'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'PriceCycleOscillator': 1.0
        })
    )
