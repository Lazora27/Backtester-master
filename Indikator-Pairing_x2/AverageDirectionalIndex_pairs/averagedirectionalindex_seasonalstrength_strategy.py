import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageDirectionalIndex_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageDirectionalIndex und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'AverageDirectionalIndex': {
                'class': AverageDirectionalIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageDirectionalIndex'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'AverageDirectionalIndex': 1.0,
            'SeasonalStrength': 1.0
        })
    )
