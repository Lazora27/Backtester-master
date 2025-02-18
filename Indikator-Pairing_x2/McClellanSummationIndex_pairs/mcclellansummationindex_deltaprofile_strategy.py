import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanSummationIndex_DeltaProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanSummationIndex und DeltaProfile
    """
    
    params = (
        ('indicators', {
            'McClellanSummationIndex': {
                'class': McClellanSummationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanSummationIndex'>
            },
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            }
        }),
        ('weights', {
            'McClellanSummationIndex': 1.0,
            'DeltaProfile': 1.0
        })
    )
