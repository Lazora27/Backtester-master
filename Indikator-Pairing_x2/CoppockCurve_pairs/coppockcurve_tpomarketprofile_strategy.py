import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CoppockCurve_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CoppockCurve und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'CoppockCurve': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
