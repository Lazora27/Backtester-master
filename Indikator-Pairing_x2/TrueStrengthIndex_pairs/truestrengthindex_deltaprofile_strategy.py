import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueStrengthIndex_DeltaProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueStrengthIndex und DeltaProfile
    """
    
    params = (
        ('indicators', {
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            },
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            }
        }),
        ('weights', {
            'TrueStrengthIndex': 1.0,
            'DeltaProfile': 1.0
        })
    )
