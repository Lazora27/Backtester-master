import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_PriceCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und PriceCycleOscillator
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'PriceCycleOscillator': {
                'class': PriceCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceCycleOscillator'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'PriceCycleOscillator': 1.0
        })
    )
