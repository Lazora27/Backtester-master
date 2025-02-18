import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeDelta_PriceCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeDelta und PriceCycleOscillator
    """
    
    params = (
        ('indicators', {
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            },
            'PriceCycleOscillator': {
                'class': PriceCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceCycleOscillator'>
            }
        }),
        ('weights', {
            'VolumeDelta': 1.0,
            'PriceCycleOscillator': 1.0
        })
    )
