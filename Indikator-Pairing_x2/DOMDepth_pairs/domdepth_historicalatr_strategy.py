import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_HistoricalATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und HistoricalATR
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'HistoricalATR': 1.0
        })
    )
