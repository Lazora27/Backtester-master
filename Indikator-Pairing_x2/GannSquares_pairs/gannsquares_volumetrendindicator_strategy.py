import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquares_VolumeTrendIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquares und VolumeTrendIndicator
    """
    
    params = (
        ('indicators', {
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            },
            'VolumeTrendIndicator': {
                'class': VolumeTrendIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeTrendIndicator'>
            }
        }),
        ('weights', {
            'GannSquares': 1.0,
            'VolumeTrendIndicator': 1.0
        })
    )
