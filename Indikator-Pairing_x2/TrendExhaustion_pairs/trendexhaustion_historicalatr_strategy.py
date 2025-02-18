import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_HistoricalATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und HistoricalATR
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'HistoricalATR': 1.0
        })
    )
