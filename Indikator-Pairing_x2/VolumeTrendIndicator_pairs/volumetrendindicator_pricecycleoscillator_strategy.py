import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeTrendIndicator_PriceCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeTrendIndicator und PriceCycleOscillator
    """
    
    params = (
        ('indicators', {
            'VolumeTrendIndicator': {
                'class': VolumeTrendIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeTrendIndicator'>
            },
            'PriceCycleOscillator': {
                'class': PriceCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceCycleOscillator'>
            }
        }),
        ('weights', {
            'VolumeTrendIndicator': 1.0,
            'PriceCycleOscillator': 1.0
        })
    )
