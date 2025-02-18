import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ParabolicSAR_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ParabolicSAR und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'ParabolicSAR': 1.0,
            'SeasonalStrength': 1.0
        })
    )
