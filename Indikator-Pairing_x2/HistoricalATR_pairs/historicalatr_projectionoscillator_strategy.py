import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalATR_ProjectionOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalATR und ProjectionOscillator
    """
    
    params = (
        ('indicators', {
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            },
            'ProjectionOscillator': {
                'class': ProjectionOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionOscillator'>
            }
        }),
        ('weights', {
            'HistoricalATR': 1.0,
            'ProjectionOscillator': 1.0
        })
    )
