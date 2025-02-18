import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AccelerationBands_CyberCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AccelerationBands und CyberCycleOscillator
    """
    
    params = (
        ('indicators', {
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            },
            'CyberCycleOscillator': {
                'class': CyberCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycleOscillator'>
            }
        }),
        ('weights', {
            'AccelerationBands': 1.0,
            'CyberCycleOscillator': 1.0
        })
    )
