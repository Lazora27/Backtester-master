import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PivotPoints_HistoricalATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PivotPoints und HistoricalATR
    """
    
    params = (
        ('indicators', {
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            },
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            }
        }),
        ('weights', {
            'PivotPoints': 1.0,
            'HistoricalATR': 1.0
        })
    )
