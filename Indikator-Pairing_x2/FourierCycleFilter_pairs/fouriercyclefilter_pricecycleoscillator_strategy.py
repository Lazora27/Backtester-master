import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FourierCycleFilter_PriceCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FourierCycleFilter und PriceCycleOscillator
    """
    
    params = (
        ('indicators', {
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            },
            'PriceCycleOscillator': {
                'class': PriceCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceCycleOscillator'>
            }
        }),
        ('weights', {
            'FourierCycleFilter': 1.0,
            'PriceCycleOscillator': 1.0
        })
    )
