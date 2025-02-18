import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
