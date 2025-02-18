import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und TimeCycle
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'TimeCycle': 1.0
        })
    )
