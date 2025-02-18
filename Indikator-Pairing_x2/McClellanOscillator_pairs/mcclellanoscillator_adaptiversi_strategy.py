import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanOscillator_AdaptiveRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanOscillator und AdaptiveRSI
    """
    
    params = (
        ('indicators', {
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            },
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            }
        }),
        ('weights', {
            'McClellanOscillator': 1.0,
            'AdaptiveRSI': 1.0
        })
    )
