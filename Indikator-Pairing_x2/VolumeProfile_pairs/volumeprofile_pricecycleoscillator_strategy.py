import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeProfile_PriceCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeProfile und PriceCycleOscillator
    """
    
    params = (
        ('indicators', {
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            },
            'PriceCycleOscillator': {
                'class': PriceCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceCycleOscillator'>
            }
        }),
        ('weights', {
            'VolumeProfile': 1.0,
            'PriceCycleOscillator': 1.0
        })
    )
