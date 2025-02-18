import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SupplyDemandZones_ParabolicSAR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SupplyDemandZones und ParabolicSAR
    """
    
    params = (
        ('indicators', {
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            },
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            }
        }),
        ('weights', {
            'SupplyDemandZones': 1.0,
            'ParabolicSAR': 1.0
        })
    )
