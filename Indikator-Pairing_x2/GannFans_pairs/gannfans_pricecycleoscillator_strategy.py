import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannFans_PriceCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannFans und PriceCycleOscillator
    """
    
    params = (
        ('indicators', {
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            },
            'PriceCycleOscillator': {
                'class': PriceCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceCycleOscillator'>
            }
        }),
        ('weights', {
            'GannFans': 1.0,
            'PriceCycleOscillator': 1.0
        })
    )
