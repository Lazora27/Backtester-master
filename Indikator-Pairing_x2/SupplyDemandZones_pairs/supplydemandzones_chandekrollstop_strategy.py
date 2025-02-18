import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SupplyDemandZones_ChandeKrollStop_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SupplyDemandZones und ChandeKrollStop
    """
    
    params = (
        ('indicators', {
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            },
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            }
        }),
        ('weights', {
            'SupplyDemandZones': 1.0,
            'ChandeKrollStop': 1.0
        })
    )
