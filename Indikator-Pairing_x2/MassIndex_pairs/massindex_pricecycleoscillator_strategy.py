import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MassIndex_PriceCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MassIndex und PriceCycleOscillator
    """
    
    params = (
        ('indicators', {
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            },
            'PriceCycleOscillator': {
                'class': PriceCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceCycleOscillator'>
            }
        }),
        ('weights', {
            'MassIndex': 1.0,
            'PriceCycleOscillator': 1.0
        })
    )
