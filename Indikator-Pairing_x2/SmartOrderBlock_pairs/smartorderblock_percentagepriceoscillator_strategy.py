import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_PercentagePriceOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und PercentagePriceOscillator
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'PercentagePriceOscillator': {
                'class': PercentagePriceOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PercentagePriceOscillator'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'PercentagePriceOscillator': 1.0
        })
    )
