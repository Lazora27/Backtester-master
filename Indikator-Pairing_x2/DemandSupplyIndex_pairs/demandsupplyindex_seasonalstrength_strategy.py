import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DemandSupplyIndex_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DemandSupplyIndex und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'DemandSupplyIndex': 1.0,
            'SeasonalStrength': 1.0
        })
    )
