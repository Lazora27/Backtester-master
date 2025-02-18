import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanOscillator_SmoothedRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanOscillator und SmoothedRSI
    """
    
    params = (
        ('indicators', {
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            },
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            }
        }),
        ('weights', {
            'McClellanOscillator': 1.0,
            'SmoothedRSI': 1.0
        })
    )
