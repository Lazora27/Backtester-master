import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalATR_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalATR und CCITurbo
    """
    
    params = (
        ('indicators', {
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'HistoricalATR': 1.0,
            'CCITurbo': 1.0
        })
    )
