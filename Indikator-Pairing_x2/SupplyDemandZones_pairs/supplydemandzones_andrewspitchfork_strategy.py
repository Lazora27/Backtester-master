import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SupplyDemandZones_AndrewsPitchfork_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SupplyDemandZones und AndrewsPitchfork
    """
    
    params = (
        ('indicators', {
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            },
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            }
        }),
        ('weights', {
            'SupplyDemandZones': 1.0,
            'AndrewsPitchfork': 1.0
        })
    )
