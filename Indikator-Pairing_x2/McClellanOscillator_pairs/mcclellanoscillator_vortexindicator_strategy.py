import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanOscillator_VortexIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanOscillator und VortexIndicator
    """
    
    params = (
        ('indicators', {
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            },
            'VortexIndicator': {
                'class': VortexIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VortexIndicator'>
            }
        }),
        ('weights', {
            'McClellanOscillator': 1.0,
            'VortexIndicator': 1.0
        })
    )
