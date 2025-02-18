import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_CoppockCurve_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und CoppockCurve
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'CoppockCurve': 1.0
        })
    )
