import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_DeltaProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und DeltaProfile
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'DeltaProfile': 1.0
        })
    )
