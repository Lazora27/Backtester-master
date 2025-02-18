import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SupplyDemandZones_TapeReading_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SupplyDemandZones und TapeReading
    """
    
    params = (
        ('indicators', {
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            },
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            }
        }),
        ('weights', {
            'SupplyDemandZones': 1.0,
            'TapeReading': 1.0
        })
    )
