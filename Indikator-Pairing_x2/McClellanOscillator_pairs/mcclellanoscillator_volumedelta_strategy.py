import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanOscillator_VolumeDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanOscillator und VolumeDelta
    """
    
    params = (
        ('indicators', {
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            },
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            }
        }),
        ('weights', {
            'McClellanOscillator': 1.0,
            'VolumeDelta': 1.0
        })
    )
