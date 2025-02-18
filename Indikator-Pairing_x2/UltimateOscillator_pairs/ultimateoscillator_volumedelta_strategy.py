import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UltimateOscillator_VolumeDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UltimateOscillator und VolumeDelta
    """
    
    params = (
        ('indicators', {
            'UltimateOscillator': {
                'class': UltimateOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UltimateOscillator1'>
            },
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            }
        }),
        ('weights', {
            'UltimateOscillator': 1.0,
            'VolumeDelta': 1.0
        })
    )
