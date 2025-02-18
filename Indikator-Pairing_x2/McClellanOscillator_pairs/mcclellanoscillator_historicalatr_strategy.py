import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanOscillator_HistoricalATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanOscillator und HistoricalATR
    """
    
    params = (
        ('indicators', {
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            },
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            }
        }),
        ('weights', {
            'McClellanOscillator': 1.0,
            'HistoricalATR': 1.0
        })
    )
