import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_AverageDirectionalIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und AverageDirectionalIndex
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'AverageDirectionalIndex': {
                'class': AverageDirectionalIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageDirectionalIndex'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'AverageDirectionalIndex': 1.0
        })
    )
