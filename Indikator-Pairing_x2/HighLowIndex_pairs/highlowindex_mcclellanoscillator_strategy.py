import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_McClellanOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und McClellanOscillator
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'McClellanOscillator': 1.0
        })
    )
