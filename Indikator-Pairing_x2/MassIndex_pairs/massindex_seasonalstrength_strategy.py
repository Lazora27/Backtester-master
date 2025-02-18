import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MassIndex_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MassIndex und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'MassIndex': 1.0,
            'SeasonalStrength': 1.0
        })
    )
