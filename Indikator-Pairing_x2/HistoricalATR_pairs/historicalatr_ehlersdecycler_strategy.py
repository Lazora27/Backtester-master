import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalATR_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalATR und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'HistoricalATR': 1.0,
            'EhlersDecycler': 1.0
        })
    )
