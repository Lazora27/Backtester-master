import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EldersForceIndex_HistoricalATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EldersForceIndex und HistoricalATR
    """
    
    params = (
        ('indicators', {
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            },
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            }
        }),
        ('weights', {
            'EldersForceIndex': 1.0,
            'HistoricalATR': 1.0
        })
    )
