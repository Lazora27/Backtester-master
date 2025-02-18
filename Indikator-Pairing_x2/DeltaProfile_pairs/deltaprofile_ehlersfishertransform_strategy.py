import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
