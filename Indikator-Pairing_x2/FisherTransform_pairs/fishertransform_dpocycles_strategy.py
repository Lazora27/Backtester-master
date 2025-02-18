import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und DPOCycles
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'DPOCycles': 1.0
        })
    )
