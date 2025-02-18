import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CoppockCurve_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CoppockCurve und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'CoppockCurve': 1.0,
            'SeasonalStrength': 1.0
        })
    )
