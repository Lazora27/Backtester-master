import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_PriceCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und PriceCycleOscillator
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'PriceCycleOscillator': {
                'class': PriceCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceCycleOscillator'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'PriceCycleOscillator': 1.0
        })
    )
