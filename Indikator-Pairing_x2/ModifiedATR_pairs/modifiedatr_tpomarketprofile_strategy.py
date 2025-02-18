import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedATR_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedATR und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'ModifiedATR': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
