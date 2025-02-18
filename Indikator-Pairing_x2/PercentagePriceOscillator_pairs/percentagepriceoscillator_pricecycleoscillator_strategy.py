import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PercentagePriceOscillator_PriceCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PercentagePriceOscillator und PriceCycleOscillator
    """
    
    params = (
        ('indicators', {
            'PercentagePriceOscillator': {
                'class': PercentagePriceOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PercentagePriceOscillator'>
            },
            'PriceCycleOscillator': {
                'class': PriceCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceCycleOscillator'>
            }
        }),
        ('weights', {
            'PercentagePriceOscillator': 1.0,
            'PriceCycleOscillator': 1.0
        })
    )
