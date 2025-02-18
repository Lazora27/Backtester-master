import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_ParabolicSAR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und ParabolicSAR
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'ParabolicSAR': 1.0
        })
    )
