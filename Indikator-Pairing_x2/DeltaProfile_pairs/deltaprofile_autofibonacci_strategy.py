import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_AutoFibonacci_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und AutoFibonacci
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'AutoFibonacci': 1.0
        })
    )
