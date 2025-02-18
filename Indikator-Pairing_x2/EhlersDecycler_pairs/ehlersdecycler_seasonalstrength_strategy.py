import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EhlersDecycler_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EhlersDecycler und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'EhlersDecycler': 1.0,
            'SeasonalStrength': 1.0
        })
    )
