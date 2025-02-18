import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedPutCallRatio_DeltaProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedPutCallRatio und DeltaProfile
    """
    
    params = (
        ('indicators', {
            'WeightedPutCallRatio': {
                'class': WeightedPutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedPutCallRatio'>
            },
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            }
        }),
        ('weights', {
            'WeightedPutCallRatio': 1.0,
            'DeltaProfile': 1.0
        })
    )
