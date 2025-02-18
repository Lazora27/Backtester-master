import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanOscillator_TickActivityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanOscillator und TickActivityIndex
    """
    
    params = (
        ('indicators', {
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            },
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            }
        }),
        ('weights', {
            'McClellanOscillator': 1.0,
            'TickActivityIndex': 1.0
        })
    )
