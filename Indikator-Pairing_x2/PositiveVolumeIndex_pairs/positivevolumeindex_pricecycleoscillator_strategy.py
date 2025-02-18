import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PositiveVolumeIndex_PriceCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PositiveVolumeIndex und PriceCycleOscillator
    """
    
    params = (
        ('indicators', {
            'PositiveVolumeIndex': {
                'class': PositiveVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PositiveVolumeIndex'>
            },
            'PriceCycleOscillator': {
                'class': PriceCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceCycleOscillator'>
            }
        }),
        ('weights', {
            'PositiveVolumeIndex': 1.0,
            'PriceCycleOscillator': 1.0
        })
    )
