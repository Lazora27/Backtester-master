import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_McClellanOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und McClellanOscillator
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'McClellanOscillator': 1.0
        })
    )
