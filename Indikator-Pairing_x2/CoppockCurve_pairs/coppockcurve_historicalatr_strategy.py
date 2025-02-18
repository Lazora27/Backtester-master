import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CoppockCurve_HistoricalATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CoppockCurve und HistoricalATR
    """
    
    params = (
        ('indicators', {
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            },
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            }
        }),
        ('weights', {
            'CoppockCurve': 1.0,
            'HistoricalATR': 1.0
        })
    )
