import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageLogRange_PriceCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageLogRange und PriceCycleOscillator
    """
    
    params = (
        ('indicators', {
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            },
            'PriceCycleOscillator': {
                'class': PriceCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceCycleOscillator'>
            }
        }),
        ('weights', {
            'AverageLogRange': 1.0,
            'PriceCycleOscillator': 1.0
        })
    )
