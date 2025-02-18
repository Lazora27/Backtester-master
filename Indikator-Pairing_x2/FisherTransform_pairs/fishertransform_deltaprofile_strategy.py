import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_DeltaProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und DeltaProfile
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'DeltaProfile': 1.0
        })
    )
