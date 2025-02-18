import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanOscillator_NegativeVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanOscillator und NegativeVolumeIndex
    """
    
    params = (
        ('indicators', {
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            },
            'NegativeVolumeIndex': {
                'class': NegativeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NegativeVolumeIndex'>
            }
        }),
        ('weights', {
            'McClellanOscillator': 1.0,
            'NegativeVolumeIndex': 1.0
        })
    )
