import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanOscillator_MassIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanOscillator und MassIndex
    """
    
    params = (
        ('indicators', {
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            },
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            }
        }),
        ('weights', {
            'McClellanOscillator': 1.0,
            'MassIndex': 1.0
        })
    )
