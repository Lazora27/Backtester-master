import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
