import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPBands_HistoricalATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPBands und HistoricalATR
    """
    
    params = (
        ('indicators', {
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            },
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            }
        }),
        ('weights', {
            'VWAPBands': 1.0,
            'HistoricalATR': 1.0
        })
    )
