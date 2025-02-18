import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BuyingPressure_PriceCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BuyingPressure und PriceCycleOscillator
    """
    
    params = (
        ('indicators', {
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            },
            'PriceCycleOscillator': {
                'class': PriceCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceCycleOscillator'>
            }
        }),
        ('weights', {
            'BuyingPressure': 1.0,
            'PriceCycleOscillator': 1.0
        })
    )
