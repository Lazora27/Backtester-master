import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannFans_HistoricalATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannFans und HistoricalATR
    """
    
    params = (
        ('indicators', {
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            },
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            }
        }),
        ('weights', {
            'GannFans': 1.0,
            'HistoricalATR': 1.0
        })
    )
