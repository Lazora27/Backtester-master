import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SupplyDemandZones_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SupplyDemandZones und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'SupplyDemandZones': 1.0,
            'EhlersDecycler': 1.0
        })
    )
