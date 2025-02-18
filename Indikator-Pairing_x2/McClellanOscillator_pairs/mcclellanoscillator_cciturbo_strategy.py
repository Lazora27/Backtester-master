import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanOscillator_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanOscillator und CCITurbo
    """
    
    params = (
        ('indicators', {
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'McClellanOscillator': 1.0,
            'CCITurbo': 1.0
        })
    )
