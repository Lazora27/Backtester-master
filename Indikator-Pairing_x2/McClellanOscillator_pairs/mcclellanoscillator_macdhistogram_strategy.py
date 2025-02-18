import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanOscillator_MACDHistogram_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanOscillator und MACDHistogram
    """
    
    params = (
        ('indicators', {
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            },
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            }
        }),
        ('weights', {
            'McClellanOscillator': 1.0,
            'MACDHistogram': 1.0
        })
    )
