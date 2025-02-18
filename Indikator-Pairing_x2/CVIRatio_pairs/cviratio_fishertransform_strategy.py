import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_FisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und FisherTransform
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'FisherTransform': 1.0
        })
    )
