import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoFibonacci_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoFibonacci und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'AutoFibonacci': 1.0,
            'SeasonalStrength': 1.0
        })
    )
