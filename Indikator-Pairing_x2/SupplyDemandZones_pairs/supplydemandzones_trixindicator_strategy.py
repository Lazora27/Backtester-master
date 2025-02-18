import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SupplyDemandZones_TRIXIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SupplyDemandZones und TRIXIndicator
    """
    
    params = (
        ('indicators', {
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            },
            'TRIXIndicator': {
                'class': TRIXIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TRIXIndicator'>
            }
        }),
        ('weights', {
            'SupplyDemandZones': 1.0,
            'TRIXIndicator': 1.0
        })
    )
