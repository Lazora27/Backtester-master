import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_HighLowIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und HighLowIndex
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'HighLowIndex': 1.0
        })
    )
