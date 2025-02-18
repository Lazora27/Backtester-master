import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueStrengthIndex_SupplyDemandZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueStrengthIndex und SupplyDemandZones
    """
    
    params = (
        ('indicators', {
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            },
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            }
        }),
        ('weights', {
            'TrueStrengthIndex': 1.0,
            'SupplyDemandZones': 1.0
        })
    )
