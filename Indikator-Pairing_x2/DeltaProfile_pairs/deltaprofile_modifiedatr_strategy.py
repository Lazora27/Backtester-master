import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'ModifiedATR': 1.0
        })
    )
