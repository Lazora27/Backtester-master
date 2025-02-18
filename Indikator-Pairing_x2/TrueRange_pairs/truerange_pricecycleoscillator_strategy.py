import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueRange_PriceCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueRange und PriceCycleOscillator
    """
    
    params = (
        ('indicators', {
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            },
            'PriceCycleOscillator': {
                'class': PriceCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceCycleOscillator'>
            }
        }),
        ('weights', {
            'TrueRange': 1.0,
            'PriceCycleOscillator': 1.0
        })
    )
