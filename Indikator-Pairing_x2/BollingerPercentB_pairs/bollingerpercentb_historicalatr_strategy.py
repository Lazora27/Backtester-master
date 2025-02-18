import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerPercentB_HistoricalATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerPercentB und HistoricalATR
    """
    
    params = (
        ('indicators', {
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            },
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            }
        }),
        ('weights', {
            'BollingerPercentB': 1.0,
            'HistoricalATR': 1.0
        })
    )
