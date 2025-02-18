import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanOscillator_WilliamsR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanOscillator und WilliamsR
    """
    
    params = (
        ('indicators', {
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            },
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            }
        }),
        ('weights', {
            'McClellanOscillator': 1.0,
            'WilliamsR': 1.0
        })
    )
