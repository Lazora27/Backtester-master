import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanOscillator_TickIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanOscillator und TickIndex
    """
    
    params = (
        ('indicators', {
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            },
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            }
        }),
        ('weights', {
            'McClellanOscillator': 1.0,
            'TickIndex': 1.0
        })
    )
