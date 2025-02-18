import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanOscillator_MomentumIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanOscillator und MomentumIndicator
    """
    
    params = (
        ('indicators', {
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            },
            'MomentumIndicator': {
                'class': MomentumIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumIndicator'>
            }
        }),
        ('weights', {
            'McClellanOscillator': 1.0,
            'MomentumIndicator': 1.0
        })
    )
