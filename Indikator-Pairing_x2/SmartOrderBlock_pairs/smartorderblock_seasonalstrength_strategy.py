import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'SeasonalStrength': 1.0
        })
    )
