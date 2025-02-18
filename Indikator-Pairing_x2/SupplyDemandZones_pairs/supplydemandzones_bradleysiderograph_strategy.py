import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SupplyDemandZones_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SupplyDemandZones und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'SupplyDemandZones': 1.0,
            'BradleySiderograph': 1.0
        })
    )
