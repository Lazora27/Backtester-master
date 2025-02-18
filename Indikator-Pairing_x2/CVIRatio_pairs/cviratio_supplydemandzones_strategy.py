import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_SupplyDemandZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und SupplyDemandZones
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'SupplyDemandZones': 1.0
        })
    )
