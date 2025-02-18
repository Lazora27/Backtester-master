import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanOscillator_McClellanSummationIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanOscillator und McClellanSummationIndex
    """
    
    params = (
        ('indicators', {
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            },
            'McClellanSummationIndex': {
                'class': McClellanSummationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanSummationIndex'>
            }
        }),
        ('weights', {
            'McClellanOscillator': 1.0,
            'McClellanSummationIndex': 1.0
        })
    )
