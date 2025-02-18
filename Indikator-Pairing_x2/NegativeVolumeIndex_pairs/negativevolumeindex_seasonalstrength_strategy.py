import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NegativeVolumeIndex_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NegativeVolumeIndex und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'NegativeVolumeIndex': {
                'class': NegativeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NegativeVolumeIndex'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'NegativeVolumeIndex': 1.0,
            'SeasonalStrength': 1.0
        })
    )
