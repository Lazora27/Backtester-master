import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_VolatilityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und VolatilityIndex
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'VolatilityIndex': {
                'class': VolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolatilityIndex'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'VolatilityIndex': 1.0
        })
    )
