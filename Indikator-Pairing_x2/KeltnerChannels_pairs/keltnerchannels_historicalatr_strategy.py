import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KeltnerChannels_HistoricalATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KeltnerChannels und HistoricalATR
    """
    
    params = (
        ('indicators', {
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            },
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            }
        }),
        ('weights', {
            'KeltnerChannels': 1.0,
            'HistoricalATR': 1.0
        })
    )
