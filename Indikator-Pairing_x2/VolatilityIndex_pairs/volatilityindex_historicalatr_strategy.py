import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolatilityIndex_HistoricalATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolatilityIndex und HistoricalATR
    """
    
    params = (
        ('indicators', {
            'VolatilityIndex': {
                'class': VolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolatilityIndex'>
            },
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            }
        }),
        ('weights', {
            'VolatilityIndex': 1.0,
            'HistoricalATR': 1.0
        })
    )
