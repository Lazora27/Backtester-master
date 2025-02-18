import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinOscillator_HistoricalATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinOscillator und HistoricalATR
    """
    
    params = (
        ('indicators', {
            'ChaikinOscillator': {
                'class': ChaikinOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinOscillator'>
            },
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            }
        }),
        ('weights', {
            'ChaikinOscillator': 1.0,
            'HistoricalATR': 1.0
        })
    )
