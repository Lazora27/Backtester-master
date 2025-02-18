import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_DeltaProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und DeltaProfile
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'DeltaProfile': 1.0
        })
    )
