import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DPOCycles_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DPOCycles und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'DPOCycles': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
