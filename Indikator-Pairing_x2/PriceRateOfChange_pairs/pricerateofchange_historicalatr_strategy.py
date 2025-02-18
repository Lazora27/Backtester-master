import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceRateOfChange_HistoricalATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceRateOfChange und HistoricalATR
    """
    
    params = (
        ('indicators', {
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            },
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            }
        }),
        ('weights', {
            'PriceRateOfChange': 1.0,
            'HistoricalATR': 1.0
        })
    )
