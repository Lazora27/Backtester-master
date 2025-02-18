import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedATR_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedATR und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'ModifiedATR': 1.0,
            'SeasonalStrength': 1.0
        })
    )
