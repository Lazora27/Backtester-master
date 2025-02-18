import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_DeltaProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und DeltaProfile
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'DeltaProfile': 1.0
        })
    )
