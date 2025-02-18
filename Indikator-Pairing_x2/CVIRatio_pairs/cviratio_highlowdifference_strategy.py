import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_HighLowDifference_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und HighLowDifference
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'HighLowDifference': 1.0
        })
    )
