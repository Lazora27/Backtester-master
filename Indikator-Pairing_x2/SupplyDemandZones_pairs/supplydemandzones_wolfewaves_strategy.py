import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SupplyDemandZones_WolfeWaves_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SupplyDemandZones und WolfeWaves
    """
    
    params = (
        ('indicators', {
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            },
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            }
        }),
        ('weights', {
            'SupplyDemandZones': 1.0,
            'WolfeWaves': 1.0
        })
    )
