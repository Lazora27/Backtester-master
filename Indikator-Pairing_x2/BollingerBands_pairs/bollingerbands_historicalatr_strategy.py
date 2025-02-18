import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBands_HistoricalATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBands und HistoricalATR
    """
    
    params = (
        ('indicators', {
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            },
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            }
        }),
        ('weights', {
            'BollingerBands': 1.0,
            'HistoricalATR': 1.0
        })
    )
