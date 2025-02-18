import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_PriceCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und PriceCycleOscillator
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'PriceCycleOscillator': {
                'class': PriceCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceCycleOscillator'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'PriceCycleOscillator': 1.0
        })
    )
