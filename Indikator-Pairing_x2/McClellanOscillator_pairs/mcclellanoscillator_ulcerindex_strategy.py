import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanOscillator_UlcerIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanOscillator und UlcerIndex
    """
    
    params = (
        ('indicators', {
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            },
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            }
        }),
        ('weights', {
            'McClellanOscillator': 1.0,
            'UlcerIndex': 1.0
        })
    )
