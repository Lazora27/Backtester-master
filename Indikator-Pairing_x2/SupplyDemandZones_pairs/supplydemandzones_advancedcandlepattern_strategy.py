import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SupplyDemandZones_AdvancedCandlePattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SupplyDemandZones und AdvancedCandlePattern
    """
    
    params = (
        ('indicators', {
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            },
            'AdvancedCandlePattern': {
                'class': AdvancedCandlePattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvancedCandlePattern'>
            }
        }),
        ('weights', {
            'SupplyDemandZones': 1.0,
            'AdvancedCandlePattern': 1.0
        })
    )
