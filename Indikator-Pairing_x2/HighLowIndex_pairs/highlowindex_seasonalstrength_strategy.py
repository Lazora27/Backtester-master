import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'SeasonalStrength': 1.0
        })
    )
