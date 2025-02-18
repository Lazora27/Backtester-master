import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanSummationIndex_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanSummationIndex und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'McClellanSummationIndex': {
                'class': McClellanSummationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanSummationIndex'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'McClellanSummationIndex': 1.0,
            'SeasonalStrength': 1.0
        })
    )
