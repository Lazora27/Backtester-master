import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SupplyDemandZones_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SupplyDemandZones und CCITurbo
    """
    
    params = (
        ('indicators', {
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'SupplyDemandZones': 1.0,
            'CCITurbo': 1.0
        })
    )
