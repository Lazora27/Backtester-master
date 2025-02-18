import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SupplyDemandZones_VWAPDeviationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SupplyDemandZones und VWAPDeviationBands
    """
    
    params = (
        ('indicators', {
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            },
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            }
        }),
        ('weights', {
            'SupplyDemandZones': 1.0,
            'VWAPDeviationBands': 1.0
        })
    )
