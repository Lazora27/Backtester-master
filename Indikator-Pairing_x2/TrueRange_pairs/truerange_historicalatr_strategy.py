import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueRange_HistoricalATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueRange und HistoricalATR
    """
    
    params = (
        ('indicators', {
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            },
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            }
        }),
        ('weights', {
            'TrueRange': 1.0,
            'HistoricalATR': 1.0
        })
    )
