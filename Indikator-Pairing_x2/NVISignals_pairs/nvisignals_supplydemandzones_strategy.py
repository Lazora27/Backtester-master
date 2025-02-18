import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_SupplyDemandZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und SupplyDemandZones
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'SupplyDemandZones': 1.0
        })
    )
