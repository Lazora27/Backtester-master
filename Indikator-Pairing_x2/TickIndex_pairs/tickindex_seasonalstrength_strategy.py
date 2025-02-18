import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'SeasonalStrength': 1.0
        })
    )
