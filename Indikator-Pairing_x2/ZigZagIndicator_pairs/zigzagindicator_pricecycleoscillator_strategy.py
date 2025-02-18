import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ZigZagIndicator_PriceCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ZigZagIndicator und PriceCycleOscillator
    """
    
    params = (
        ('indicators', {
            'ZigZagIndicator': {
                'class': ZigZagIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZigZagIndicator'>
            },
            'PriceCycleOscillator': {
                'class': PriceCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceCycleOscillator'>
            }
        }),
        ('weights', {
            'ZigZagIndicator': 1.0,
            'PriceCycleOscillator': 1.0
        })
    )
