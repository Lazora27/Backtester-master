import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanOscillator_PutCallRatio_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanOscillator und PutCallRatio
    """
    
    params = (
        ('indicators', {
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            },
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            }
        }),
        ('weights', {
            'McClellanOscillator': 1.0,
            'PutCallRatio': 1.0
        })
    )
