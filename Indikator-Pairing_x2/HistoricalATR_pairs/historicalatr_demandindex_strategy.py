import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalATR_DemandIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalATR und DemandIndex
    """
    
    params = (
        ('indicators', {
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            },
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            }
        }),
        ('weights', {
            'HistoricalATR': 1.0,
            'DemandIndex': 1.0
        })
    )
