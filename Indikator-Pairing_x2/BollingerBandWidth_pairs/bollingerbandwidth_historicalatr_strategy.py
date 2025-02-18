import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBandWidth_HistoricalATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBandWidth und HistoricalATR
    """
    
    params = (
        ('indicators', {
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            },
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            }
        }),
        ('weights', {
            'BollingerBandWidth': 1.0,
            'HistoricalATR': 1.0
        })
    )
