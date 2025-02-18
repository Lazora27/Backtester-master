import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_ChaikinVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und ChaikinVolatility
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'ChaikinVolatility': 1.0
        })
    )
