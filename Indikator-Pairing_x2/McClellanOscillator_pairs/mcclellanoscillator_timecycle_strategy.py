import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanOscillator_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanOscillator und TimeCycle
    """
    
    params = (
        ('indicators', {
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'McClellanOscillator': 1.0,
            'TimeCycle': 1.0
        })
    )
