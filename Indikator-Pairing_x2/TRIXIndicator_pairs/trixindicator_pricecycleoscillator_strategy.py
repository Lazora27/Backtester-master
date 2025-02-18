import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TRIXIndicator_PriceCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TRIXIndicator und PriceCycleOscillator
    """
    
    params = (
        ('indicators', {
            'TRIXIndicator': {
                'class': TRIXIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TRIXIndicator'>
            },
            'PriceCycleOscillator': {
                'class': PriceCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceCycleOscillator'>
            }
        }),
        ('weights', {
            'TRIXIndicator': 1.0,
            'PriceCycleOscillator': 1.0
        })
    )
