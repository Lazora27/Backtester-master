import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SupplyDemandZones_HistoricalATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SupplyDemandZones und HistoricalATR
    """
    
    params = (
        ('indicators', {
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            },
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            }
        }),
        ('weights', {
            'SupplyDemandZones': 1.0,
            'HistoricalATR': 1.0
        })
    )
