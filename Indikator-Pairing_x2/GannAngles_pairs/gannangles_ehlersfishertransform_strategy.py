import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannAngles_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannAngles und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'GannAngles': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
