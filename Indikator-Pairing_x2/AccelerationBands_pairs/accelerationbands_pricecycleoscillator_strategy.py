import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AccelerationBands_PriceCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AccelerationBands und PriceCycleOscillator
    """
    
    params = (
        ('indicators', {
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            },
            'PriceCycleOscillator': {
                'class': PriceCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceCycleOscillator'>
            }
        }),
        ('weights', {
            'AccelerationBands': 1.0,
            'PriceCycleOscillator': 1.0
        })
    )
