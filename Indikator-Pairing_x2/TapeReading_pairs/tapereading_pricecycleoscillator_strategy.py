import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_PriceCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und PriceCycleOscillator
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'PriceCycleOscillator': {
                'class': PriceCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceCycleOscillator'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'PriceCycleOscillator': 1.0
        })
    )
