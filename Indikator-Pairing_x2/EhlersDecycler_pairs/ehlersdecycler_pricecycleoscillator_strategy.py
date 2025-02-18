import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EhlersDecycler_PriceCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EhlersDecycler und PriceCycleOscillator
    """
    
    params = (
        ('indicators', {
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            },
            'PriceCycleOscillator': {
                'class': PriceCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceCycleOscillator'>
            }
        }),
        ('weights', {
            'EhlersDecycler': 1.0,
            'PriceCycleOscillator': 1.0
        })
    )
