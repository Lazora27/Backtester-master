import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanOscillator_ModifiedRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanOscillator und ModifiedRSI
    """
    
    params = (
        ('indicators', {
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            },
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            }
        }),
        ('weights', {
            'McClellanOscillator': 1.0,
            'ModifiedRSI': 1.0
        })
    )
