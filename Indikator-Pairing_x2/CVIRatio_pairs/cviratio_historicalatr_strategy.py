import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_HistoricalATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und HistoricalATR
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'HistoricalATR': 1.0
        })
    )
