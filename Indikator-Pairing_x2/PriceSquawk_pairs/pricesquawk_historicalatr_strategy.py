import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_HistoricalATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und HistoricalATR
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'HistoricalATR': 1.0
        })
    )
