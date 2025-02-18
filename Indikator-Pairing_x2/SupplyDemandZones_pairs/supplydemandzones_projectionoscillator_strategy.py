import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SupplyDemandZones_ProjectionOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SupplyDemandZones und ProjectionOscillator
    """
    
    params = (
        ('indicators', {
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            },
            'ProjectionOscillator': {
                'class': ProjectionOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionOscillator'>
            }
        }),
        ('weights', {
            'SupplyDemandZones': 1.0,
            'ProjectionOscillator': 1.0
        })
    )
