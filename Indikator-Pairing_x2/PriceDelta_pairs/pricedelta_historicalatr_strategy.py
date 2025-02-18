import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_HistoricalATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und HistoricalATR
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'HistoricalATR': 1.0
        })
    )
