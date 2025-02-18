import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StandardDeviationIndicator_HistoricalATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StandardDeviationIndicator und HistoricalATR
    """
    
    params = (
        ('indicators', {
            'StandardDeviationIndicator': {
                'class': StandardDeviationIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StandardDeviationIndicator'>
            },
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            }
        }),
        ('weights', {
            'StandardDeviationIndicator': 1.0,
            'HistoricalATR': 1.0
        })
    )
