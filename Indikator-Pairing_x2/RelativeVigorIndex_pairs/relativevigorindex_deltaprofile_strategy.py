import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeVigorIndex_DeltaProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeVigorIndex und DeltaProfile
    """
    
    params = (
        ('indicators', {
            'RelativeVigorIndex': {
                'class': RelativeVigorIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVigorIndex'>
            },
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            }
        }),
        ('weights', {
            'RelativeVigorIndex': 1.0,
            'DeltaProfile': 1.0
        })
    )
