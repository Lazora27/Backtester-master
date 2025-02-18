import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UlcerIndex_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UlcerIndex und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'UlcerIndex': 1.0,
            'SeasonalStrength': 1.0
        })
    )
