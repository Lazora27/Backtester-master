import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CycleFinder_PriceCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CycleFinder und PriceCycleOscillator
    """
    
    params = (
        ('indicators', {
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            },
            'PriceCycleOscillator': {
                'class': PriceCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceCycleOscillator'>
            }
        }),
        ('weights', {
            'CycleFinder': 1.0,
            'PriceCycleOscillator': 1.0
        })
    )
