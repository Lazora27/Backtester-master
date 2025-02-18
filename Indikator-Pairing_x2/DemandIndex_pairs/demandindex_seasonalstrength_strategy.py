import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DemandIndex_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DemandIndex und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'DemandIndex': 1.0,
            'SeasonalStrength': 1.0
        })
    )
