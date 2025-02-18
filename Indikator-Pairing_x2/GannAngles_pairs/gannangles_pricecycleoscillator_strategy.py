import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannAngles_PriceCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannAngles und PriceCycleOscillator
    """
    
    params = (
        ('indicators', {
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            },
            'PriceCycleOscillator': {
                'class': PriceCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceCycleOscillator'>
            }
        }),
        ('weights', {
            'GannAngles': 1.0,
            'PriceCycleOscillator': 1.0
        })
    )
