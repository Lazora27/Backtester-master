import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IchimokuCloud_HistoricalATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IchimokuCloud und HistoricalATR
    """
    
    params = (
        ('indicators', {
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            },
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            }
        }),
        ('weights', {
            'IchimokuCloud': 1.0,
            'HistoricalATR': 1.0
        })
    )
