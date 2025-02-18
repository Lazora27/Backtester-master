import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_AverageDirectionalIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und AverageDirectionalIndex
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'AverageDirectionalIndex': {
                'class': AverageDirectionalIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageDirectionalIndex'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'AverageDirectionalIndex': 1.0
        })
    )
