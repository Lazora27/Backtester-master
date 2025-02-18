import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PolarizedTimePrice_PriceCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PolarizedTimePrice und PriceCycleOscillator
    """
    
    params = (
        ('indicators', {
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            },
            'PriceCycleOscillator': {
                'class': PriceCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceCycleOscillator'>
            }
        }),
        ('weights', {
            'PolarizedTimePrice': 1.0,
            'PriceCycleOscillator': 1.0
        })
    )
