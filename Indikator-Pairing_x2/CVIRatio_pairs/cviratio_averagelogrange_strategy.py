import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'AverageLogRange': 1.0
        })
    )
