import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeStrengthIndex_SupplyDemandZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeStrengthIndex und SupplyDemandZones
    """
    
    params = (
        ('indicators', {
            'RelativeStrengthIndex': {
                'class': RelativeStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeStrengthIndex1'>
            },
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            }
        }),
        ('weights', {
            'RelativeStrengthIndex': 1.0,
            'SupplyDemandZones': 1.0
        })
    )
