import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_SupplyDemandZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und SupplyDemandZones
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'SupplyDemandZones': 1.0
        })
    )
